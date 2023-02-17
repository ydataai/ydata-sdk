from ydata.sdk.datasources.models.datasources.googlecloudstorage import GCSDataSource as mDataSource
from ydata.sdk.datasources.datasource import DataSource

from typing import Optional

from ydata.sdk.common.client import Client, get_client
from ydata.sdk.common.config import LOG_LEVEL
from ydata.sdk.common.logger import create_logger
from ydata.sdk.common.types import UID
from ydata.sdk.connectors.connector import Connector

class GCSDataSource(DataSource):

    def __init__(self, connector: Connector, path: str, datatype: str = 'tabular', filetype: str = 'csv', separator: str = ",", name: Optional[str] = None, wait_for_metadata: bool = True, client: Optional[Client] = None):
        config = {
            "fileType": filetype,
            "separator": separator,
            "dataType": datatype,
            "path": path
        }
        #self._model = self._create_model(connector, mDataSource, config, name=name)

        # connector: Connector, datasource_type: Type[mDataSource], config: dict, name: Optional[str] = None, wait_for_metadata: bool = True, client: Optional[Client] = None
        DataSource.__init__(self, connector=connector, datasource_type=mDataSource, config=config, name=name, wait_for_metadata=wait_for_metadata, client=client)