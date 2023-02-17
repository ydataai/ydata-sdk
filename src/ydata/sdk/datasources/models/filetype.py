from enum import Enum


class FileType(Enum):
    AVRO = 'avro'
    CSV = 'csv'
    EXCEL = 'xlsx'
    PARQUET = 'parquet'

    @classmethod
    def _missing_(cls, value):
        if value in ('xls', 'excel'):
            return cls('xlsx')

        raise ValueError(f'value {value} is not allowed')
