from typing import Optional, Union

from ydata.sdk.common.client import Client
from ydata.sdk.connectors.connector import Connector
from ydata.sdk.datasources.__models.datatype import DataSourceType
from ydata.sdk.datasources.__models.filetype import FileType
from ydata.sdk.datasources.datasource import DataSource


class GCSDataSource(DataSource):

    def __init__(self, connector: Connector, path: str, datatype: Optional[Union[DataSourceType, str]] = DataSourceType.TABULAR, filetype: Union[FileType, str] = FileType.CSV, separator: str = ",", name: Optional[str] = None, wait_for_metadata: bool = True, client: Optional[Client] = None):
        config = {
            "fileType": FileType(filetype).value,
            "separator": separator,
            "path": path
        }
        DataSource.__init__(self, connector=connector, datatype=datatype,
                            name=name, wait_for_metadata=wait_for_metadata, client=client, **config)
