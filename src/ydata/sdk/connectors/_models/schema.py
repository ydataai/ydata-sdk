from typing import List, Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ydata.sdk.common.pydantic_utils import to_camel
from ydata.sdk.common.model import BaseModel


class BaseConfig(BaseModel.Config):
    alias_generator = to_camel


class TableColumn(BaseModel):
    """Class to store the information of a Column table."""

    name: str
    variable_type: str  # change this to the datatypes
    primary_key: Optional[bool]
    is_foreign_key: Optional[bool]
    foreign_keys: list
    nullable: bool

    Config = BaseConfig


class Table(BaseModel):
    """Class to store the table columns information."""

    name: str
    columns: List[TableColumn]
    primary_keys: List[TableColumn]
    foreign_keys: List[TableColumn]

    Config = BaseConfig


class Schema(BaseModel):
    """Class to store the database schema information."""

    name: str
    tables: Optional[List[Table]] = Field(None)

    Config = BaseConfig
