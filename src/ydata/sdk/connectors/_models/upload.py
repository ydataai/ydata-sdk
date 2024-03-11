from typing import Optional

from pydantic import Field

from ydata.sdk.common.model import BaseModel


class Upload(BaseModel):
    uid: str
    chunk_size: int = Field(alias='chunkSize')
    file_name: str = Field(alias='fileName')
    written_bytes: Optional[int] = Field(None, alias='writtenBytes')
    total_bytes: Optional[int] = Field(None, alias='totalBytes')
