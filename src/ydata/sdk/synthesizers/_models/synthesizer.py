from typing import Optional

from pydantic import Field
from ydata.sdk.common.model import BaseModel

from .status import Status


class Synthesizer(BaseModel):
    uid: Optional[str] = Field(None)
    author: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    status: Optional[Status] = Field(None)
