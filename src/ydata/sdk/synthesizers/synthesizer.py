from abc import ABC, abstractmethod
from io import StringIO
from time import sleep
from typing import Optional, Union
from uuid import uuid4

from pandas import DataFrame as pdDataFrame
from pandas import read_csv
from typeguard import typechecked

from ydata.sdk.common.client import Client, get_client
from ydata.sdk.common.config import BACKOFF, LOG_LEVEL
from ydata.sdk.common.exceptions import AlreadyFittedError, DataSourceNotAvailableError, NotInitializedError
from ydata.sdk.common.logger import create_logger
from ydata.sdk.datasources.datasource import DataSource, Metadata
from ydata.sdk.datasources.models.status import Status as dsStatus
from ydata.sdk.synthesizers.models.status import Status
from ydata.sdk.synthesizers.models.synthesizer import Synthesizer as mSynthesizer
from ydata.sdk.synthesizers.models.synthesizer_type import SynthesizerType
from ydata.sdk.synthesizers.models.synthesizers_list import SynthesizersList
from ydata.sdk.utils.model_mixin import ModelMixin
from ydata.sdk.utils.model_utils import filter_dict


@typechecked
class BaseSynthesizer(ABC, ModelMixin):
    """Base class for all synthesizer variants.

    Methods
    -------
    - `fit`: train a synthesizer instance.

    - `sample`: request synthetic data.

    - `status`: current status of the synthesizer instance.
    """

    def __init__(self, client: Optional[Client] = None):
        """Initialize the synthesizer.

        Note:
            The synthesizer instance is created in the backend only when the `fit` method is called.

        Arguments:
            client (Client): (optional) Client to connet to the backend
        """
        self._client = get_client(client)
        self._logger = create_logger(__name__, level=LOG_LEVEL)

        self._model: Optional[mSynthesizer] = None

    def fit(self, X: Union[DataSource, pdDataFrame], metadata: Optional[Metadata] = None, target: Optional[str] = None, name: Optional[str] = None) -> None:  # TODO: Target + data
        """Initialize the object.

        Arguments:
            X (Union[DataSource, pdDataFrame]): Training dataset
            metadata (Metadata): (optional) Metadata associated to the datasource
            target (Optional[str]): (optional) Metadata associated to the datasource
            anonymize (dict): (optional) Anonymizer configuration
        """
        if self._is_initialized():
            raise AlreadyFittedError()

        # If the training data is a pandas dataframe, we first need to create a data source and then the instance
        if isinstance(X, pdDataFrame):
            _X = DataSource(source=X, client=self._client)
        else:
            _X = X

        if _X.status != dsStatus.AVAILABLE:
            raise DataSourceNotAvailableError(
                f"The datasource '{_X.uid}' is not available (status = {_X.status.value})")

        self._fit_from_datasource(X=_X, metadata=metadata, name=name)

    @staticmethod
    def _metadata_to_payload(metadata: Metadata) -> list:
        columns = []
        for c in metadata.columns:
            columns.append({
                'name': c.name,
                'generation': True,
                'dataType': c.datatype,
                'varType': c.vartype,
                'entity': False
            })
        return columns

    def _fit_from_datasource(self, X: DataSource, metadata: Optional[Metadata] = None, name: Optional[str] = None) -> None:
        _name = name if name is not None else str(uuid4())
        # TODO: update based on the user input as well
        columns = self._metadata_to_payload(X.metadata)
        payload = {
            'name': _name,
            'dataSourceUID': X.uid,
            'metadata': {
                'dataType': 'tabular',  # TODO: From Datasource / or specified by the user for DataFrame
                "columns": columns,
            },
        }

        response = self._client.post('/synthesizer/', json=payload)
        data: list = response.json()
        self._model, _ = self._model_from_api(X.datatype, data)

    @staticmethod
    def _model_from_api(datatype: str, data: dict) -> mSynthesizer:
        from ydata.sdk.synthesizers.models.synthesizer_map import TYPE_TO_CLASS
        synth_cls = TYPE_TO_CLASS.get(SynthesizerType(datatype).value)
        data['status'] = synth_cls._resolve_api_status(data['status'])
        data = filter_dict(mSynthesizer, data)
        return mSynthesizer(**data), synth_cls

    @abstractmethod
    def sample(self) -> pdDataFrame:
        """Abstract method to sample from a synthesizer."""

    def _sample(self, payload: dict) -> pdDataFrame:
        response = self._client.post(
            f"/synthesizer/{self.model.uid}/sample", json=payload)

        data: dict = response.json()
        sample_uid = data.get('uid')
        sample_status = None
        while sample_status != 'finished':  # TODO: timeout :)
            print('Sampling from the synthesizer...')
            response = self._client.get(f'/synthesizer/{self.model.uid}/history')
            history: dict = response.json()
            sample_data = next((s for s in history if s.get('uid') == sample_uid), None)
            sample_status = sample_data['state']
            sleep(BACKOFF)

        response = self._client.get_static_file(
            f'/synthesizer/{self.model.uid}/sample/{sample_uid}/sample.csv')
        data = StringIO(response.content.decode())
        return read_csv(data)

    def status(self) -> Status:
        """Get the status of a synthesizer instance."""
        if not self._is_initialized():
            return Status.NOT_INITIALIZED

        try:
            self = self.get(self._model.uid, self._client)
            return self.model.status
        except Exception:  # noqa: PIE786
            return Status.UNKNOWN

    @staticmethod
    def get(id: str, client: Optional[Client] = None) -> SynthesizersList:
        """List the synthesizer instances.

        Arguments:
            client (Client): (optional) Client to connet to the backend
        """
        _client = get_client(client)
        response = _client.get(f'/synthesizer/{id}')

        data: list = response.json()
        model, synth_cls = BaseSynthesizer._model_from_api(
            data['dataSource']['dataType'], data)
        return ModelMixin._init_from_model_data(synth_cls, model)

    @staticmethod
    def list(client: Optional[Client] = None) -> SynthesizersList:
        """List the synthesizer instances.

        Arguments:
            client (Client): (optional) Client to connet to the backend
        """
        def __process_data(data: list) -> list:
            to_del = ['metadata', 'report', 'mode']
            for e in data:
                for k in to_del:
                    e.pop(k, None)
            return data

        _client = get_client(client)
        response = _client.get('/synthesizer')
        data: list = response.json()
        data = __process_data(data)

        return SynthesizersList(data)

    def _is_initialized(self) -> bool:
        return self._model is not None

    @property
    def model(self) -> mSynthesizer:  # TODO: Should not expose fully the model
        if not self._is_initialized():
            raise NotInitializedError()
        return self._model

    @staticmethod
    def _resolve_api_status(api_status: dict) -> Status:
        return Status(api_status.get('state', Status.UNKNOWN.name))
