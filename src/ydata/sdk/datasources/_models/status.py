from pydantic import BaseModel

from ydata.core.enum import StringEnum


class ValidationState(StringEnum):
    PREPARING = 'preparing'
    VALIDATING = 'validating'
    AVAILABLE = 'available'
    FAILED = 'failed'
    UNKNOWN = 'unknown'


class Status(StringEnum):
    """Represent the status of a [`DataSource`][ydata.sdk.datasources.datasource.DataSource]."""

    AVAILABLE = 'available'
    """The [`DataSource`][ydata.sdk.datasources.datasource.DataSource] is available and ready to be used.
    """

    PREPARING = 'preparing'
    """The [`DataSource`][ydata.sdk.datasources.datasource.DataSource] is being prepared.
    """

    VALIDATING = 'validating'
    """The [`DataSource`][ydata.sdk.datasources.datasource.DataSource] is being validated.
    """

    FAILED = 'failed'
    """The [`DataSource`][ydata.sdk.datasources.datasource.DataSource] preparation or validation has failed.
    """

    UNAVAILABLE = 'unavailable'
    """The [`DataSource`][ydata.sdk.datasources.datasource.DataSource] is unavailable at the moment.
    """

    UNKNOWN = 'unknown'
    """The [`DataSource`][ydata.sdk.datasources.datasource.DataSource] status could not be retrieved.
    """


class State(BaseModel):
    validation: str
    metadata: str
    profiling: str
