from dataclasses import dataclass

from ydata.sdk.datasources._models.datasource import DataSource
from ydata.sdk.datasources._models.filetype import FileType


@dataclass
class AWSS3DataSource(DataSource):

    filetype: FileType = None
    path: str = None
    separator: str = ','

    def to_payload(self):
        return {
            'fileType': FileType(self.filetype).value,
            'path': self.path,
            'separator': self.separator
        }
