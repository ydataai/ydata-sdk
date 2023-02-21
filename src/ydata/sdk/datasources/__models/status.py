from pydantic import BaseModel

from ydata.core.enum import StringEnum


class ValidationState(StringEnum):
    PREPARING = 'preparing'
    VALIDATING = 'validating'
    AVAILABLE = 'available'
    FAILED = 'failed'
    UNKNOWN = 'unknown'


class Status(StringEnum):
    AVAILABLE = 'available'
    PREPARING = 'preparing'
    VALIDATING = 'validating'
    FAILED = 'failed'
    UNKNOWN = 'unknown'


class State(BaseModel):
    validation: str
    metadata: str
    profiling: str
