from typing import Optional

from pydantic import Field

from ydata.sdk.connectors._models.schema import Schema

from .connector import Connector


class RDBMSConnector(Connector):
    db_schema: Optional[Schema] = Field(None, alias="schema")
