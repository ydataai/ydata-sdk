from typing import Optional

from pydantic import Field

from .connector import Connector


class LocalConnector(Connector):
    file: Optional[str] = Field(None)
