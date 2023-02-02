from typing import Generic, TypeVar

from pydantic import BaseModel

from ydata.core.enum import StringEnum

T = TypeVar("T")


class GenericStateErrorStatus(BaseModel, Generic[T]):
    state: T


class PrepareState(StringEnum):
    PREPARING = 'preparing'
    DISCOVERING = 'discovering'
    FINISHED = 'finished'
    FAILED = 'failed'


class TrainingState(StringEnum):
    PREPARING = 'preparing'
    RUNNING = 'running'
    FINISHED = 'finished'
    FAILED = 'failed'


class ReportState(StringEnum):
    UNKNOWN = 'unknown'
    DISCOVERING = 'discovering'
    FINISHED = 'finished'
    FAILED = 'failed'


PrepareStatus = GenericStateErrorStatus[PrepareState]
TrainingStatus = GenericStateErrorStatus[TrainingState]
ReportStatus = GenericStateErrorStatus[ReportState]


class Status(StringEnum):
    NOT_INITIALIZED = 'not initialized'
    PREPARE = 'prepare'
    TRAIN = 'train'
    REPORT = 'report'  # Should not be here for SDK
    READY = 'ready'
    UNKNOWN = 'unknown'
