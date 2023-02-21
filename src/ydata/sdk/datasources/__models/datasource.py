from dataclasses import dataclass
from typing import Optional

from ydata.sdk.datasources.__models.datatype import DataSourceType
from ydata.sdk.datasources.__models.metadata.metadata import Metadata
from ydata.sdk.datasources.__models.status import State, Status


@dataclass
class DataSource():  # BaseModel):

    uid: Optional[str] = None
    author: Optional[str] = None
    name: Optional[str] = None
    datatype: Optional[DataSourceType] = None
    metadata: Optional[Metadata] = None
    status: Optional[Status] = None
    state: Optional[State] = None

    def __post_init__(self):
        if self.metadata is not None:
            self.metadata = Metadata(**self.metadata)

        if self.state is not None:
            data = {
                'validation': self.state['state'],
                'metadata': self.state['state'],
                'profiling': self.state['state']
            }
            self.state = State.parse_obj(data)

        if self.status is not None:
            self.status = Status(self.status)
