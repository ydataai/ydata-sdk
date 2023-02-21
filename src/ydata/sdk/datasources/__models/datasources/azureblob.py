from dataclasses import dataclass

from ydata.sdk.datasources.__models.datasource import DataSource
from ydata.sdk.datasources.__models.filetype import FileType


@dataclass
class AzureBlobDataSource(DataSource):

    filetype: FileType = None
    path: str = None
