from pydantic import BaseModel

from ydata.sdk.datasources.__models.metadata.warning_types import Level, WarningType


class Details(BaseModel):
    level: Level
    value: str

    class Config:
        use_enum_values = True


class MetadataWarning(BaseModel):
    column: str
    details: Details
    type: WarningType

    class Config:
        use_enum_values = True
