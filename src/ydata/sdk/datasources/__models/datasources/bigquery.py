from dataclasses import dataclass

from ydata.sdk.datasources.__models.datasource import DataSource


@dataclass
class BigQueryDataSource(DataSource):

    query: str = None
