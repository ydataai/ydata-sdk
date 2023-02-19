from typing import List

from pydantic import Field

from ydata.sdk.common.model import BaseModel


class DatasourceAttrs(BaseModel):
    sortbykey: List[str] = Field(default_factory=list)
    entity_id_cols: List[str] = Field(default_factory=list)
    generate_cols: List[str] = Field(default_factory=list)
    exclude_cols: List[str] = Field(default_factory=list)
