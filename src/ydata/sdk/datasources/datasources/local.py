from ydata.sdk.datasources.models.datasource import DataSource as mDataSource
from ydata.sdk.datasources.datasource import DataSource

from typing import Optional

from ydata.sdk.common.client import Client, get_client
from ydata.sdk.common.config import LOG_LEVEL
from ydata.sdk.common.logger import create_logger


from io import BytesIO
from pathlib import Path
from typing import Optional, Union
from uuid import uuid4

from pandas import DataFrame as pdDataFrame

from ydata.sdk.common.client import Client, get_client
from ydata.sdk.common.config import LOG_LEVEL
from ydata.sdk.common.logger import create_logger
from ydata.sdk.connectors.connector import Connector
from ydata.sdk.datasources.models.datasource import DataSource as mDataSource
from ydata.sdk.utils.model_mixin import ModelMixin


class LocalDataSource(DataSource):

    def __init__(self, source: Optional[Union[pdDataFrame, str, Path]] = None, datatype: str = 'tabular', filetype: str = 'csv', separator: str = ",", name: Optional[str] = None, client: Optional[Client] = None):
        self._client = get_client(client)
        self._logger = create_logger(__name__, level=LOG_LEVEL)
        self._model: Optional[mDataSource] = None

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

        config = {
            "fileType": filetype,
            "separator": separator,
            "dataType": datatype
        }

        self._model = DataSource.create(
            connector, mDataSource, config=config, name=_name, client=self._client)._model