from pydantic import BaseModel

from ydata.core.enum import StringEnum


class Status(StringEnum):
    AVAILABLE = 'available'
    PREPARING = 'preparing'
    VALIDATING = 'validating'
    UNKNOWN = 'unknown'

# @dataclass


class State(BaseModel):
    validation: str
    metadata: str
    profiling: str
