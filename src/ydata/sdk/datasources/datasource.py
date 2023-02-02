from io import BytesIO
from pathlib import Path
from time import sleep
from typing import Optional, Union
from uuid import uuid4

from pandas import DataFrame as pdDataFrame

from ydata.sdk.common.client import Client, get_client
from ydata.sdk.common.config import BACKOFF, LOG_LEVEL
from ydata.sdk.common.logger import create_logger
from ydata.sdk.common.types import UID
from ydata.sdk.connectors.connector import Connector
from ydata.sdk.datasources.models.datasource import DataSource as mDataSource
from ydata.sdk.datasources.models.datasource_list import DataSourceList
from ydata.sdk.datasources.models.status import Status
from ydata.sdk.utils.model_mixin import ModelMixin
from ydata.sdk.utils.model_utils import filter_dict


class DataSource(ModelMixin):
    def __init__(self, source: Optional[Union[pdDataFrame, str, Path]] = None, name: Optional[str] = None, client: Optional[Client] = None):
        self._client = get_client(client)
        self._logger = create_logger(__name__, level=LOG_LEVEL)
        self._model: Optional[mDataSource] = None

        if source is not None:
            if isinstance(source, str):
                source = Path(source)

            if isinstance(source, pdDataFrame):
                buffer = BytesIO()
                source.to_csv(buffer)
                buffer.seek(0)
                files = {'file': buffer}
            else:
                files = {'file': source.open('rb')}

            _name = name if name is not None else str(uuid4())
            data = {
                "type": 'file',
                "name": f"{_name}_connector"
            }

            response = self._client.post('/connector/', data=data, files=files)
            data: list = response.json()
            model = Connector._model_from_api(data)
            connector = ModelMixin._init_from_model_data(Connector, model)

            payload = {
                "name": _name,
                "fileType": "csv",
                "separator": ",",
                "dataType": "tabular",
                "connector": {
                    "uid": connector.uid,
                    "type": connector.type
                }
            }

            response = self._client.post('/datasource/', json=payload)
            data: list = response.json()
            model = DataSource._model_from_api(data)
            self._model = model

    @property
    def uid(self):
        return self._model.uid

    @property
    def datatype(self):
        return self._model.datatype

    @property
    def status(self):
        return self._model.status

    @property
    def metadata(self):
        return self._model.metadata

    @staticmethod
    def list(client: Optional[Client] = None) -> DataSourceList:
        def __process_data(data: list) -> list:
            to_del = ['metadata']
            for e in data:
                for k in to_del:
                    e.pop(k, None)
            return data

        _client = get_client(client)
        response = _client.get('/datasource')
        data: list = response.json()
        data = __process_data(data)

        return DataSourceList(data)

    @staticmethod
    def get(uid: UID, client: Optional[Client] = None) -> "DataSource":
        _client = get_client(client)
        response = _client.get(f'/datasource/{uid}')
        data: list = response.json()

        # TODO: Move to pydantic model directly
        data['datatype'] = data.pop('dataType')
        data['state'] = data['status']
        data['status'] = DataSource._resolve_api_status(data['status'])
        data = filter_dict(mDataSource, data)
        model = mDataSource(**data)
        datasource = ModelMixin._init_from_model_data(DataSource, model)
        return datasource

    @staticmethod
    def create(connector: Connector, path: str, name: Optional[str] = None, wait_for_metadata: bool = True, client: Optional[Client] = None) -> "DataSource":
        _client = get_client(client)
        _name = name if name is not None else str(uuid4())
        # TODO: Change the payload according to the connector type
        payload = {
            "name": _name,
            "path": path,  # TODO: parse properly depending on the connector type
            "fileType": "csv",
            "separator": ",",
            "dataType": "tabular",
            "connector": {
                "uid": connector.uid,
                "type": connector.type
            }
        }

        response = _client.post('/datasource/', json=payload)
        data: list = response.json()
        model = DataSource._model_from_api(data)
        datasource = ModelMixin._init_from_model_data(DataSource, model)

        if wait_for_metadata:
            # TODO: Other "finished" status such as FAILED
            while datasource.status not in [Status.AVAILABLE]:
                print(f'Calculating metadata [{datasource.status}]')
                datasource = DataSource.get(uid=datasource.uid, client=client)
                sleep(BACKOFF)

        return datasource

    @staticmethod
    def _resolve_api_status(api_status: dict) -> Status:
        return Status(api_status.get('state', Status.UNKNOWN.name))

    @staticmethod
    def _model_from_api(data: dict) -> mDataSource:
        data['datatype'] = data.pop('dataType')
        data['state'] = data['status']
        data['status'] = DataSource._resolve_api_status(data['status'])
        data = filter_dict(mDataSource, data)
        model = mDataSource(**data)
        return model
