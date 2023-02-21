from ydata.core.enum import StringEnum


class DataSourceType(StringEnum):
    TABULAR = "tabular"
    """The [`DataSource`][ydata.sdk.datasources.datasource.DataSource] is tabular (i.e. it does not have a temporal dimension).
    """
    TIMESERIES = "timeseries"
    """The [`DataSource`][ydata.sdk.datasources.datasource.DataSource] has a temporal dimension.
    """
