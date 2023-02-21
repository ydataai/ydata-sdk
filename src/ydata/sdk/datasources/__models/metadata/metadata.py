from typing import List, Optional

from pydantic import BaseModel, Field

from ydata.sdk.datasources.__models.metadata.column import Column
from ydata.sdk.datasources.__models.metadata.warnings import MetadataWarning


class Cardinality(BaseModel):
    column: str
    value: int


class LongTextStatistics(BaseModel):
    average_number_of_characters: int = Field(alias="averageNumberOfCharacters")
    average_number_of_words: int = Field(alias="averageNumberOfWords")


class Metadata(BaseModel):
    cardinality: Optional[List[Cardinality]] = Field(None)
    columns: List[Column]
    duplicate_rows: int = Field(alias="duplicateRows")
    long_text_statistics: Optional[LongTextStatistics] = Field(
        None, alias="longTextStatistics")
    memory: str
    missing_cells: int = Field(alias="missingCells")
    number_of_rows: int = Field(alias="numberOfRows")
    warnings: Optional[List[MetadataWarning]] = Field(None)

    def __repr__(self) -> str:
        columns = ',\n  '.join([str(c) for c in self.columns])
        return f"""Metadata(columns=[
    {columns}
])"""

    def __str__(self) -> str:
        return self.__repr__()
