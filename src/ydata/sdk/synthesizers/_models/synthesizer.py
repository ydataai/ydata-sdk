from typing import Optional

from pydantic import BaseModel, Field

from .status import Status


class Synthesizer(BaseModel):
    uid: Optional[str] = Field(None)
    author: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    status: Optional[Status] = Field(None)
