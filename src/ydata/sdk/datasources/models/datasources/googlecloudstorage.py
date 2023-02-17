from pydantic import Field
from dataclasses import dataclass, field

from ydata.sdk.datasources.models.datasource import DataSource
from ydata.sdk.datasources.models.filetype import FileType


@dataclass
class GCSDataSource(DataSource):

  filetype: FileType = None# = Field(alias='fileType')
  path: str = None
