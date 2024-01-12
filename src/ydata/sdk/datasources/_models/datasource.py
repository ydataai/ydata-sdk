from dataclasses import dataclass

from ydata.sdk.common.types import UID
from ydata.sdk.datasources._models.datatype import DataSourceType
from ydata.sdk.datasources._models.metadata.metadata import Metadata
from ydata.sdk.datasources._models.status import Status


@dataclass
class DataSource:

    uid: UID | None = None
    author: str | None = None
    name: str | None = None
    datatype: DataSourceType | None = None
    metadata: Metadata | None = None
    status: Status | None = None

    def to_payload(self):
        return {}
