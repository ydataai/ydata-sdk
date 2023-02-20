from time import sleep
from typing import Optional, Type, Union
from uuid import uuid4

from ydata.sdk.common.client import Client
from ydata.sdk.common.client.utils import init_client
from ydata.sdk.common.config import BACKOFF, LOG_LEVEL
from ydata.sdk.common.logger import create_logger
from ydata.sdk.common.types import UID
from ydata.sdk.connectors.connector import Connector
from ydata.sdk.datasources.models.datasource import DataSource as mDataSource
from ydata.sdk.datasources.models.datasource_list import DataSourceList
from ydata.sdk.datasources.models.datatype import DataSourceType
from ydata.sdk.datasources.models.status import Status, ValidationState
from ydata.sdk.utils.model_mixin import ModelMixin
from ydata.sdk.utils.model_utils import filter_dict


class DataSource(ModelMixin):

    def __init__(self, connector: Connector, datatype: Optional[Union[DataSourceType, str]] = DataSourceType.TABULAR, name: Optional[str] = None, wait_for_metadata: bool = True, client: Optional[Client] = None, **config):
        from ydata.sdk.datasources.models.connector_to_datasource import CONN_TO_DS
        datasource_type = CONN_TO_DS.get(connector.type)
        self._init_common(client=client)
        self._model: Optional[mDataSource] = self._create_model(
            connector=connector, datasource_type=datasource_type, datatype=datatype, config=config, name=name, client=self._client)

        if wait_for_metadata:
            self._model = DataSource._wait_for_metadata(self)._model

    @init_client
    def _init_common(self, client: Optional[Client] = None):
        self._client = client
        self._logger = create_logger(__name__, level=LOG_LEVEL)

    @property
    def uid(self):
        return self._model.uid

    @property
    def datatype(self):
        return self._model.datatype

    @property
    def status(self):
        try:
            self = self.get(self._model.uid, self._client)
            return self._model.status
        except Exception:  # noqa: PIE786
            return Status.UNKNOWN

    @property
    def metadata(self):
        return self._model.metadata

    @staticmethod
    @init_client
    def list(client: Optional[Client] = None) -> DataSourceList:
        def __process_data(data: list) -> list:
            to_del = ['metadata']
            for e in data:
                for k in to_del:
                    e.pop(k, None)
            return data

        response = client.get('/datasource')
        data: list = response.json()
        data = __process_data(data)

        return DataSourceList(data)

    @staticmethod
    @init_client
    def get(uid: UID, client: Optional[Client] = None) -> "DataSource":
        response = client.get(f'/datasource/{uid}')
        data: list = response.json()

        # TODO: Move to pydantic model directly
        data['datatype'] = data.pop('dataType')
        data['state'] = data['status']
        data['status'] = DataSource._resolve_api_status(data['status'])
        data = filter_dict(mDataSource, data)
        model = mDataSource(**data)
        datasource = ModelMixin._init_from_model_data(DataSource, model)
        return datasource

    @classmethod
    def create(cls, connector: Connector, datatype: Optional[Union[DataSourceType, str]] = DataSourceType.TABULAR, name: Optional[str] = None, wait_for_metadata: bool = True, client: Optional[Client] = None, **kwargs) -> "DataSource":
        from ydata.sdk.datasources.models.connector_to_datasource import CONN_TO_DS
        datasource_type = CONN_TO_DS.get(connector.type)
        return cls._create(connector=connector, datasource_type=datasource_type, datatype=datatype, config=kwargs, name=name, wait_for_metadata=wait_for_metadata, client=client)

    @classmethod
    def _create(cls, connector: Connector, datasource_type: Type[mDataSource], datatype: Optional[Union[DataSourceType, str]] = DataSourceType.TABULAR, config: Optional[dict] = None, name: Optional[str] = None, wait_for_metadata: bool = True, client: Optional[Client] = None) -> "DataSource":
        model = DataSource._create_model(
            connector, datasource_type, datatype, config, name, client)
        datasource = ModelMixin._init_from_model_data(DataSource, model)

        if wait_for_metadata:
            datasource = DataSource._wait_for_metadata(datasource)

        return datasource

    @classmethod
    @init_client
    def _create_model(cls, connector: Connector, datasource_type: Type[mDataSource], datatype: Optional[Union[DataSourceType, str]] = DataSourceType.TABULAR, config: Optional[dict] = None, name: Optional[str] = None, client: Optional[Client] = None) -> mDataSource:
        _name = name if name is not None else str(uuid4())
        _config = config if config is not None else {}
        payload = {
            "name": _name,
            "connector": {
                "uid": connector.uid,
                "type": connector.type.value
            },
            "dataType": datatype.value
        }
        payload.update(_config)
        response = client.post('/datasource/', json=payload)
        data: list = response.json()
        return DataSource._model_from_api(data, datasource_type)

    @staticmethod
    def _wait_for_metadata(datasource):
        # TODO: Other "finished" status such as FAILED
        while datasource.status not in [Status.AVAILABLE, Status.FAILED]:
            print(f'Calculating metadata [{datasource.status}]')
            datasource = DataSource.get(uid=datasource.uid, client=datasource._client)
            sleep(BACKOFF)
        return datasource

    @staticmethod
    def _resolve_api_status(api_status: dict) -> Status:
        status = Status(api_status.get('state', Status.UNKNOWN.name))
        validation = ValidationState(api_status.get('validation', {}).get(
            'state', ValidationState.UNKNOWN.name))
        if validation == ValidationState.FAILED:
            status = Status.FAILED
        return status

    @staticmethod
    def _model_from_api(data: dict, datasource_type: Type[mDataSource]) -> mDataSource:
        data['datatype'] = data.pop('dataType')
        data['state'] = data['status']
        data['status'] = DataSource._resolve_api_status(data['status'])
        data = filter_dict(datasource_type, data)
        model = datasource_type(**data)
        return model
