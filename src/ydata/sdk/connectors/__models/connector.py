from typing import Optional

from ydata.sdk.common.model import BaseModel
from ydata.sdk.common.types import UID
from ydata.sdk.connectors.__models.connector_type import ConnectorType


class Connector(BaseModel):

    uid: UID
    type: ConnectorType
    name: Optional[str] = None

    def __eq__(self, other: object) -> bool:  # TODO: proper comparison
        return dict(self) == dict(other)
