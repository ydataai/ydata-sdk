from dataclasses import dataclass

from ydata.sdk.datasources.models.datasource import DataSource


@dataclass
class BigQueryDataSource(DataSource):

    query: str = None
