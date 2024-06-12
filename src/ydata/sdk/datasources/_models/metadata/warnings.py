from ydata.sdk.common.model import BaseModel
from ydata.sdk.datasources._models.metadata.warning_types import Level, WarningType


class Details(BaseModel):
    level: Level
    value: str


class MetadataWarning(BaseModel):
    column: str
    details: Details
    type: WarningType
