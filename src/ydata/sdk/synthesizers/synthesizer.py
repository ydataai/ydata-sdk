from abc import ABC, abstractmethod
from io import StringIO
from time import sleep
from typing import Optional, Tuple, Type, Union
from uuid import uuid4

from pandas import DataFrame as pdDataFrame
from pandas import read_csv
from typeguard import typechecked

from ydata.sdk.common.client import Client
from ydata.sdk.common.client.utils import require_client
from ydata.sdk.common.config import BACKOFF, LOG_LEVEL
from ydata.sdk.common.exceptions import (AlreadyFittedError, DataSourceNotAvailableError, FittingError,
                                         NotInitializedError)
from ydata.sdk.common.logger import create_logger
from ydata.sdk.datasources import DataSource, LocalDataSource
from ydata.sdk.datasources.models.attributes import DataSourceAttrs
from ydata.sdk.datasources.models.datatype import DataSourceType
from ydata.sdk.datasources.models.metadata.metadata import Metadata
from ydata.sdk.datasources.models.status import Status as dsStatus
from ydata.sdk.synthesizers.models.status import PrepareState, Status
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
        self._init_common(client=client)
        self._model: Optional[mSynthesizer] = None

    @require_client
    def _init_common(self, client: Optional[Client] = None):
        self._client = client
        self._logger = create_logger(__name__, level=LOG_LEVEL)

    def fit(self, X: Union[DataSource, pdDataFrame], datatype: Optional[Union[DataSourceType, str]] = None, dataset_attrs: Optional[Union[DataSourceAttrs, dict]] = None, target: Optional[str] = None, name: Optional[str] = None) -> None:
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
            # TODO: Check that datatype is not None in this case
            _X = LocalDataSource(source=X, datatype=datatype, client=self._client)
        else:
            # TODO: is dataype is not None we should raise a warning
            # TODO: check dataset attributes validity
            _X = X

        if _X.status != dsStatus.AVAILABLE:
            raise DataSourceNotAvailableError(
                f"The datasource '{_X.uid}' is not available (status = {_X.status.value})")

        if isinstance(dataset_attrs, dict):
            dataset_attrs = DataSourceAttrs(**dataset_attrs)
        datatype = DataSourceType(datatype)
        self._fit_from_datasource(
            X=_X, dataset_attrs=dataset_attrs, target=target, name=name)

    @staticmethod
    def _metadata_to_payload(datatype: DataSourceType, ds_metadata: Metadata, dataset_attrs: Optional[DataSourceAttrs] = None) -> list:
        columns = {}
        for c in ds_metadata.columns:
            columns[c.name] = {
                'name': c.name,
                'generation': True,
                'dataType': c.datatype,
                'varType': c.vartype,
                'entity': False,
            }
        if dataset_attrs is not None:
            if datatype == DataSourceType.TIMESERIES:
                for c in ds_metadata.columns:
                    columns[c.name]['sortBy'] = c.name in dataset_attrs.sortbykey

                for c in dataset_attrs.entity_id_cols:
                    columns[c]['entity'] = True

            for c in dataset_attrs.generate_cols:
                columns[c]['generation'] = True

            for c in dataset_attrs.exclude_cols:
                columns[c]['generation'] = False

        return list(columns.values())

    def _fit_from_datasource(self, X: DataSource, dataset_attrs: Optional[DataSourceAttrs] = None, target: Optional[str] = None, name: Optional[str] = None) -> None:
        _name = name if name is not None else str(uuid4())
        columns = self._metadata_to_payload(
            DataSourceType(X.datatype), X.metadata, dataset_attrs)
        payload = {
            'name': _name,
            'dataSourceUID': X.uid,
            'metadata': {
                'dataType': X.datatype,
                "columns": columns,
            },
        }
        if target is not None:
            payload['metadata']['target'] = target

        response = self._client.post('/synthesizer/', json=payload)
        data: list = response.json()
        self._model, _ = self._model_from_api(X.datatype, data)
        while self.status not in [Status.READY, Status.FAILED]:
            print('Training the synthesizer...')
            sleep(BACKOFF)

        if self.status == Status.FAILED:
            raise FittingError('Could not train the synthesizer')

    @staticmethod
    def _model_from_api(datatype: str, data: dict) -> Tuple[mSynthesizer, Type["BaseSynthesizer"]]:
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

    @property
    def status(self) -> Status:
        """Get the status of a synthesizer instance."""
        if not self._is_initialized():
            return Status.NOT_INITIALIZED

        try:
            self = self.get(self._model.uid, self._client)
            return self._model.status
        except Exception:  # noqa: PIE786
            return Status.UNKNOWN

    @staticmethod
    @require_client
    def get(id: str, client: Optional[Client] = None) -> "BaseSynthesizer":
        """List the synthesizer instances.

        Arguments:
            client (Client): (optional) Client to connet to the backend
        """
        response = client.get(f'/synthesizer/{id}')
        data: list = response.json()
        model, synth_cls = BaseSynthesizer._model_from_api(
            data['dataSource']['dataType'], data)
        return ModelMixin._init_from_model_data(synth_cls, model)

    @staticmethod
    @require_client
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

        response = client.get('/synthesizer')
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
        status = Status(api_status.get('state', Status.UNKNOWN.name))
        prepare = PrepareState(api_status.get('prepare', {}).get(
            'state', PrepareState.UNKNOWN.name))
        if prepare == PrepareState.FAILED:
            status = Status.FAILED
        return status
