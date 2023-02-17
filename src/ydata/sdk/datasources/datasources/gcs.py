from typing import Optional

from ydata.sdk.common.client import Client
from ydata.sdk.connectors.connector import Connector
from ydata.sdk.datasources.datasource import DataSource
from ydata.sdk.datasources.models.datasources.googlecloudstorage import GCSDataSource as mDataSource


class GCSDataSource(DataSource):

    def __init__(self, connector: Connector, path: str, datatype: str = 'tabular', filetype: str = 'csv', separator: str = ",", name: Optional[str] = None, wait_for_metadata: bool = True, client: Optional[Client] = None):
        config = {
            "fileType": filetype,
            "separator": separator,
            "dataType": datatype,
            "path": path
        }
        DataSource.__init__(self, connector=connector, datasource_type=mDataSource,
                            config=config, name=name, wait_for_metadata=wait_for_metadata, client=client)
