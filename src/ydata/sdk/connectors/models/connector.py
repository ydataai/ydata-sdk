from dataclasses import dataclass
from typing import Optional
from ydata.sdk.connectors.models.connector_type import ConnectorType
from ydata.sdk.common.types import UID

#from ydata.sdk.platform.common.environment import namespace_from_env


@dataclass
class Connector():

    uid: UID
    type: ConnectorType
    name: Optional[str] = None

    def __eq__(self, other: object) -> bool:  # TODO: proper comparison
        return dict(self) == dict(other)
