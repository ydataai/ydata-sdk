from dataclasses import dataclass

from ydata.sdk.datasources.models.datasource import DataSource
from ydata.sdk.datasources.models.filetype import FileType


@dataclass
class GCSDataSource(DataSource):

    filetype: FileType = None
    path: str = None
