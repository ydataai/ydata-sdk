from dataclasses import dataclass
from typing import Optional

from ydata.sdk.common.types import UID
from ydata.sdk.datasources._models.datatype import DataSourceType
from ydata.sdk.datasources._models.metadata.metadata import Metadata
from ydata.sdk.datasources._models.status import Status


@dataclass
class DataSource:
    uid: Optional[UID] = None
    author: Optional[str] = None
    name: Optional[str] = None
    datatype: Optional[DataSourceType] = None
    metadata: Optional[Metadata] = None
    status: Optional[Status] = None

    def to_payload(self):
        return {}
