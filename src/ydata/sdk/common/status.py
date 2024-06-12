from typing import Generic, Optional, TypeVar

from pydantic import Field

from .model import BaseModel

T = TypeVar("T")


class GenericStateErrorStatus(BaseModel, Generic[T]):
    state: Optional[T] = Field(None)

    class Config:
        use_enum_values = True
