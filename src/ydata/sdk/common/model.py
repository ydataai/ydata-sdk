from pydantic import BaseModel as PydanticBaseModel
from pydantic import Extra


class BaseModel(PydanticBaseModel):
    """BaseModel replacement from pydantic.

    All datamodel from YData SDK inherits from this class.
    """
    class Config:
        allow_population_by_field_name = True
        extra = Extra.ignore
        use_enum_values = True
