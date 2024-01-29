from ydata.core.enum import StringEnum
from ydata.sdk.common.model import BaseModel


class ValidationState(StringEnum):
    UNKNOWN = 'unknown'
    VALIDATE = 'validate'
    VALIDATING = 'validating'
    FAILED = 'failed'
    AVAILABLE = 'available'


class MetadataState(StringEnum):
    UNKNOWN = 'unknown'
    GENERATE = 'generate'
    GENERATING = 'generating'
    FAILED = 'failed'
    AVAILABLE = 'available'


class ProfilingState(StringEnum):
    UNKNOWN = 'unknown'
    GENERATE = 'generate'
    GENERATING = 'generating'
    FAILED = 'failed'
    AVAILABLE = 'available'


class State(StringEnum):
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

    DELETED = 'deleted'
    """The [`DataSource`][ydata.sdk.datasources.datasource.DataSource] is to be deleted or has been deleted.
    """

    UNKNOWN = 'unknown'
    """The [`DataSource`][ydata.sdk.datasources.datasource.DataSource] status could not be retrieved.
    """


class Status(BaseModel):
    state: State
    validation: ValidationState
    metadata: MetadataState
    profiling: ProfilingState
