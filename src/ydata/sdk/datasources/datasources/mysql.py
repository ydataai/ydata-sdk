from typing import Optional, Union

from ydata.sdk.common.client import Client
from ydata.sdk.connectors.connector import Connector
from ydata.sdk.datasources._models.datatype import DataSourceType
from ydata.sdk.datasources.datasource import DataSource


class MySQLDataSource(DataSource):

    def __init__(self, connector: Connector, query: str, datatype: Optional[Union[DataSourceType, str]] = DataSourceType.TABULAR, name: Optional[str] = None, wait_for_metadata: bool = True, client: Optional[Client] = None):
        DataSource.__init__(self, connector=connector, datatype=datatype, name=name,
                            wait_for_metadata=wait_for_metadata, client=client, query=query)
