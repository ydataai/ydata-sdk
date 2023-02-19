from dataclasses import dataclass

from ydata.sdk.datasources.models.datasource import DataSource
from ydata.sdk.datasources.models.filetype import FileType


@dataclass
class GCSDataSource(DataSource):

    filetype: FileType = None
    path: str = None
    separator: str = ','

    def to_payload(self) -> dict:
        payload = self.to_payload()
        payload.update({
            'path': self.path,
            'separator': self.separator,
            'fileType': self.filetype
        })
