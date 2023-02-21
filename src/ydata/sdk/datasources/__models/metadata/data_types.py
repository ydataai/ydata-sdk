from ydata.core.enum import StringEnum


class DataType(StringEnum):
    NUMERICAL = "numerical"
    CATEGORICAL = "categorical"
    DATE = "date"
    ID = "id"
    LONGTEXT = "longtext"


class VariableType(StringEnum):
    INT = "int"
    FLOAT = "float"
    STR = "string"
    BOOL = "bool"
    DATETIME = "datetime"
    DATE = "date"
