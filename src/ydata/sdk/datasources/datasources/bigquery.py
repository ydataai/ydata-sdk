from typing import Optional, Union

from ydata.sdk.common.client import Client
from ydata.sdk.connectors.connector import Connector
from ydata.sdk.datasources.datasource import DataSource
from ydata.sdk.datasources.models.datasources.bigquery import BigQueryDataSource as mDataSource
from ydata.sdk.datasources.models.datatype import DataSourceType


class BigQueryDataSource(DataSource):

    def __init__(self, connector: Connector, query: str, datatype: Optional[Union[DataSourceType, str]] = DataSourceType.TABULAR, name: Optional[str] = None, wait_for_metadata: bool = True, client: Optional[Client] = None):
        config = {
            "dataType": DataSourceType(datatype),
            "query": query
        }
        DataSource.__init__(self, connector=connector, datasource_type=mDataSource,
                            config=config, name=name, wait_for_metadata=wait_for_metadata, client=client)
