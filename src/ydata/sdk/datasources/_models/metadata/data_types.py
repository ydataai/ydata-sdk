from ydata.core.enum import StringEnum


class DataType(StringEnum):
    NUMERICAL = "numerical"
    CATEGORICAL = "categorical"
    DATE = "date"
    LONGTEXT = "longtext"
    STR = "string"


class VariableType(StringEnum):
    INT = "int"
    FLOAT = "float"
    STR = "string"
    BOOL = "bool"
    DATETIME = "datetime"
    DATE = "date"
