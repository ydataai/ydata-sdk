from abc import ABC, abstractmethod
from io import StringIO
from time import sleep
from typing import Optional, Tuple, Type, Union
from uuid import uuid4
from warnings import warn

from pandas import DataFrame as pdDataFrame
from pandas import read_csv
from typeguard import typechecked

from ydata.sdk.common.client import Client
from ydata.sdk.common.client.utils import init_client
from ydata.sdk.common.config import BACKOFF, LOG_LEVEL
from ydata.sdk.common.exceptions import (AlreadyFittedError, DataSourceAttrsError, DataSourceNotAvailableError,
                                         DataTypeMissingError, FittingError)
from ydata.sdk.common.logger import create_logger
from ydata.sdk.common.types import UID
from ydata.sdk.common.warnings import DataSourceTypeWarning
from ydata.sdk.datasources import DataSource, LocalDataSource
from ydata.sdk.datasources._models.attributes import DataSourceAttrs
from ydata.sdk.datasources._models.datatype import DataSourceType
from ydata.sdk.datasources._models.metadata.metadata import Metadata
from ydata.sdk.datasources._models.status import Status as dsStatus
from ydata.sdk.synthesizers._models.status import PrepareState, Status
from ydata.sdk.synthesizers._models.synthesizer import Synthesizer as mSynthesizer
from ydata.sdk.synthesizers._models.synthesizer_type import SynthesizerType
from ydata.sdk.synthesizers._models.synthesizers_list import SynthesizersList
from ydata.sdk.utils.model_mixin import ModelMixin
from ydata.sdk.utils.model_utils import filter_dict


@typechecked
class BaseSynthesizer(ABC, ModelMixin):
    """Main synthesizer class.

    This class cannot be directly instanciated because of the specificities between [`RegularSynthesizer`][ydata.sdk.synthesizers.RegularSynthesizer] and [`TimeSeriesSynthesizer`][ydata.sdk.synthesizers.TimeSeriesSynthesizer] `sample` methods.

    Methods
    -------
    - `fit`: train a synthesizer instance.
    - `sample`: request synthetic data.
    - `status`: current status of the synthesizer instance.

    Note:
            The synthesizer instance is created in the backend only when the `fit` method is called.

    Arguments:
        client (Client): (optional) Client to connect to the backend
    """

    def __init__(self, client: Optional[Client] = None):
        self._init_common(client=client)
        self._model: Optional[mSynthesizer] = None

    @init_client
    def _init_common(self, client: Optional[Client] = None):
        self._client = client
        self._logger = create_logger(__name__, level=LOG_LEVEL)

    def fit(self, X: Union[DataSource, pdDataFrame], datatype: Optional[Union[DataSourceType, str]] = None, dataset_attrs: Optional[Union[DataSourceAttrs, dict]] = None, target: Optional[str] = None, name: Optional[str] = None) -> None:
        """Fit the synthesizer.

        The synthesizer accepts as training dataset either a pandas [`DataFrame`][pandas.DataFrame] directly or a YData [`DataSource`][ydata.sdk.datasources.DataSource].
        When the training dataset is a pandas [`DataFrame`][pandas.DataFrame], the argument `datatype` is required as it cannot be deduced.

        Similarly, `dataset_attrs` is mandatory for [`TimeSeries`][ydata.sdk.datasources.DataSourceType.TIMESERIES] dataset to specify the `sortbykey` columns.

        Arguments:
            X (Union[DataSource, pandas.DataFrame]): Training dataset
            datatype (Optional[Union[DataSourceType, str]]): (optional) Dataset datatype - required if `X` is a [`pandas.DataFrame`][pandas.DataFrame]
            dataset_attrs (Optional[Union[DataSourceAttrs, dict]]): (optional) Dataset attributes
            target (Optional[str]): (optional) Metadata associated to the datasource
            name (Optional[str]): (optional) Synthesizer instance name
        """
        if self._is_initialized():
            raise AlreadyFittedError()

        _datatype = DataSourceType(datatype) if isinstance(
            X, pdDataFrame) else X.datatype
        if isinstance(dataset_attrs, dict):
            dataset_attrs = DataSourceAttrs(**dataset_attrs)
        self._validate_datasource_attributes(X, dataset_attrs, _datatype)

        # If the training data is a pandas dataframe, we first need to create a data source and then the instance
        if isinstance(X, pdDataFrame):
            _X = LocalDataSource(source=X, datatype=_datatype, client=self._client)
        else:
            if _datatype is not None:
                warn("When the training data is a DataSource, the argument `datatype` is ignored.",
                     DataSourceTypeWarning)
            _X = X

        if _X.status != dsStatus.AVAILABLE:
            raise DataSourceNotAvailableError(
                f"The datasource '{_X.uid}' is not available (status = {_X.status.value})")

        if isinstance(dataset_attrs, dict):
            dataset_attrs = DataSourceAttrs(**dataset_attrs)

        self._fit_from_datasource(
            X=_X, dataset_attrs=dataset_attrs, target=target, name=name)

    @staticmethod
    def _validate_datasource_attributes(X: Union[DataSource, pdDataFrame], dataset_attrs: DataSourceAttrs, datatype: DataSourceType):
        columns = []
        if isinstance(X, pdDataFrame):
            columns = X.columns
            if datatype is None:
                raise DataTypeMissingError(
                    "Argument `datatype` is mandatory for pandas.DataFrame training data")
            datatype = DataSourceType(datatype)
        else:
            columns = [c.name for c in X.metadata.columns]

        if datatype == DataSourceType.TIMESERIES:
            if dataset_attrs is None:
                raise DataSourceAttrsError(
                    "The argument `dataset_attrs` is mandatory for timeseries datasource. The attributes must define at least one column in `sortbykey` attribute.")

        invalid_fields = {}
        for field, v in dataset_attrs.dict():
            not_in_cols = [c for c in v if c not in columns]
            if len(not_in_cols) > 0:
                invalid_fields[field] = not_in_cols

        if len(invalid_fields) > 0:
            error_msgs = ["\t- Field '{}': columns {} do not exist".format(
                f, ''.join(v)) for f, v in invalid_fields.items()]
            raise DataSourceAttrsError(
                "The dataset attributes are invalid: {}".format('\n'.join(error_msgs)))

    @staticmethod
    def _metadata_to_payload(datatype: DataSourceType, ds_metadata: Metadata, dataset_attrs: Optional[DataSourceAttrs] = None) -> list:
        """Transform a the metadata and dataset attributes into a valid
        payload.

        Arguments:
            datatype (DataSourceType): datasource type
            ds_metadata (Metadata): datasource metadata object
            dataset_attrs ( Optional[DataSourceAttrs] ): (optional) Dataset attributes

        Returns:
            payload dictionary
        """
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
        from ydata.sdk.synthesizers._models.synthesizer_map import TYPE_TO_CLASS
        synth_cls = TYPE_TO_CLASS.get(SynthesizerType(datatype).value)
        data['status'] = synth_cls._resolve_api_status(data['status'])
        data = filter_dict(mSynthesizer, data)
        return mSynthesizer(**data), synth_cls

    @abstractmethod
    def sample(self) -> pdDataFrame:
        """Abstract method to sample from a synthesizer."""

    def _sample(self, payload: dict) -> pdDataFrame:
        """Sample from a synthesizer.

        Arguments:
            payload (dict): payload configuring the sample request

        Returns:
            pandas `DataFrame`
        """
        response = self._client.post(
            f"/synthesizer/{self.uid}/sample", json=payload)

        data: dict = response.json()
        sample_uid = data.get('uid')
        sample_status = None
        while sample_status not in ['finished', 'failed']:
            print('Sampling from the synthesizer...')
            response = self._client.get(f'/synthesizer/{self.uid}/history')
            history: dict = response.json()
            sample_data = next((s for s in history if s.get('uid') == sample_uid), None)
            sample_status = sample_data['state']
            sleep(BACKOFF)

        response = self._client.get_static_file(
            f'/synthesizer/{self.uid}/sample/{sample_uid}/sample.csv')
        data = StringIO(response.content.decode())
        return read_csv(data)

    @property
    def uid(self) -> UID:
        """Get the status of a synthesizer instance.

        Returns:
            Synthesizer status
        """
        if not self._is_initialized():
            return Status.NOT_INITIALIZED

        return self._model.uid

    @property
    def status(self) -> Status:
        """Get the status of a synthesizer instance.

        Returns:
            Synthesizer status
        """
        if not self._is_initialized():
            return Status.NOT_INITIALIZED

        try:
            self = self.get(self._model.uid, self._client)
            return self._model.status
        except Exception:  # noqa: PIE786
            return Status.UNKNOWN

    @staticmethod
    @init_client
    def get(uid: str, client: Optional[Client] = None) -> "BaseSynthesizer":
        """List the synthesizer instances.

        Arguments:
            uid (str): synthesizer instance uid
            client (Client): (optional) Client to connect to the backend

        Returns:
            Synthesizer instance
        """
        response = client.get(f'/synthesizer/{uid}')
        data: list = response.json()
        model, synth_cls = BaseSynthesizer._model_from_api(
            data['dataSource']['dataType'], data)
        return ModelMixin._init_from_model_data(synth_cls, model)

    @staticmethod
    @init_client
    def list(client: Optional[Client] = None) -> SynthesizersList:
        """List the synthesizer instances.

        Arguments:
            client (Client): (optional) Client to connect to the backend

        Returns:
            List of synthesizers
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
        """Determine if a synthesizer is instanciated or not.

        Returns:
            True if the synthesizer is instanciated
        """
        return self._model is not None

    @staticmethod
    def _resolve_api_status(api_status: dict) -> Status:
        """Determine the status of the Synthesizer.

        The status of the synthesizer instance is determined by the state of
        its different components.

        Arguments:
            api_status (dict): json from the endpoint GET /synthesizer

        Returns:
            Synthesizer Status
        """
        status = Status(api_status.get('state', Status.UNKNOWN.name))
        prepare = PrepareState(api_status.get('prepare', {}).get(
            'state', PrepareState.UNKNOWN.name))
        if prepare == PrepareState.FAILED:
            status = Status.FAILED
        return status
