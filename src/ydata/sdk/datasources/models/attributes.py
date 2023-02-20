from typing import List

from pydantic import Field

from ydata.sdk.common.model import BaseModel


class DataSourceAttrs(BaseModel):
    sortbykey: List[str] = Field(default_factory=list)
    entity_id_cols: List[str] = Field(default_factory=list)
    generate_cols: List[str] = Field(default_factory=list)
    exclude_cols: List[str] = Field(default_factory=list)

    def __init__(self, **fields):
        sortbykey = fields.get("sortbykey")
        if sortbykey is not None and isinstance(sortbykey, str):
            fields['sortbykey'] = [sortbykey]

        entity_id_cols = fields.get("entity_id_cols")
        if entity_id_cols is not None and isinstance(entity_id_cols, str):
            fields['entity_id_cols'] = [entity_id_cols]

        super().__init__(**fields)
