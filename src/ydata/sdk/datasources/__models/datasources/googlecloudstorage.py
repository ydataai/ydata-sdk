from dataclasses import dataclass

from ydata.sdk.datasources.__models.datasource import DataSource
from ydata.sdk.datasources.__models.filetype import FileType


@dataclass
class GCSDataSource(DataSource):

    filetype: FileType = None
    path: str = None
    separator: str = ','
