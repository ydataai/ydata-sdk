from pydantic import BaseModel, Field

from .status import Status


class Synthesizer(BaseModel):
    uid: str | None = None
    author: str | None = None
    name: str | None = None
    status: Status | None = Field(None)
