from dataclasses import dataclass

from ydata.sdk.datasources._models.datasource import DataSource


@dataclass
class PostgreSQLDataSource(DataSource):

    query: str = None

    def to_payload(self):
        self.dict()
