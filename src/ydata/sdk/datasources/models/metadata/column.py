from typing import NewType

from pydantic import BaseModel, Field

from ydata.sdk.datasources.models.metadata.data_types import DataType, VariableType


class Column(BaseModel):

    name: str
    datatype: DataType = Field(alias='dataType')
    vartype: VariableType = Field(alias='varType')

    class Config:
        use_enum_values = True

    def __repr__(self) -> str:
        return f"Column(name={self.name}, datatype={self.datatype}, vartype={self.vartype})"

    def __str__(self) -> str:
        return super().__repr__()


TabularColumn = NewType("TabularColumn", Column)


class TimeseriesColumn(Column):
    sort_by: bool
    entity: bool
