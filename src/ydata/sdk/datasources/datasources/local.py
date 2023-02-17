from io import BytesIO
from pathlib import Path
from typing import Optional, Union
from uuid import uuid4

from pandas import DataFrame as pdDataFrame

from ydata.sdk.common.client import Client, get_client
from ydata.sdk.connectors.connector import Connector
from ydata.sdk.datasources.datasource import DataSource
from ydata.sdk.datasources.models.datasource import DataSource as mDataSource
from ydata.sdk.datasources.models.datatype import DataSourceType
from ydata.sdk.utils.model_mixin import ModelMixin


class LocalDataSource(DataSource):

    def __init__(self, source: Union[pdDataFrame, str, Path], datatype: Optional[Union[DataSourceType, str]] = DataSourceType.TABULAR, filetype: str = 'csv', separator: str = ",", name: Optional[str] = None, wait_for_metadata: bool = True, client: Optional[Client] = None):

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

        client = get_client(client)
        response = client.post('/connector/', data=data, files=files)
        data: list = response.json()
        model = Connector._model_from_api(data)
        connector = ModelMixin._init_from_model_data(Connector, model)

        config = {
            "fileType": filetype,
            "separator": separator,
            "dataType": datatype,
        }

        DataSource.__init__(self, connector=connector, datasource_type=mDataSource,
                            config=config, name=name, wait_for_metadata=wait_for_metadata, client=client)
