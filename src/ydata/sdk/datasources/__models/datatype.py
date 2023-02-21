from ydata.core.enum import StringEnum


class DataSourceType(StringEnum):
    TABULAR = "tabular"
    TIMESERIES = "timeseries"
