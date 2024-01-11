from typing import Generic, TypeVar

from pydantic import BaseModel, Field
from ydata.core.enum import StringEnum

T = TypeVar("T")


class GenericStateErrorStatus(BaseModel, Generic[T]):
    state: T | None = Field(None)

    class Config:
        use_enum_values = True


class PrepareState(StringEnum):
    PREPARING = "preparing"
    DISCOVERING = "discovering"
    FINISHED = "finished"
    FAILED = "failed"


class TrainingState(StringEnum):
    PREPARING = "preparing"
    RUNNING = "running"
    FINISHED = "finished"
    FAILED = "failed"


class ReportState(StringEnum):
    PREPARING = "preparing"
    GENERATING = "generating"
    AVAILABLE = "available"
    FAILED = "failed"


PrepareStatus = GenericStateErrorStatus[PrepareState]
TrainingStatus = GenericStateErrorStatus[TrainingState]
ReportStatus = GenericStateErrorStatus[ReportState]


class Status(BaseModel):
    class State(StringEnum):
        NOT_INITIALIZED = 'not initialized'
        UNKNOWN = 'unknown'

        PREPARE = "prepare"
        TRAIN = "train"
        REPORT = "report"
        READY = "ready"

    state: State | None = Field(None)
    prepare: PrepareStatus | None = Field(None)
    training: TrainingStatus | None = Field(None)
    report: ReportStatus | None = Field(None)

    @staticmethod
    def not_initialized() -> "Status":
        return Status(state=Status.State.NOT_INITIALIZED)

    @staticmethod
    def unknown() -> "Status":
        return Status(state=Status.State.UNKNOWN)
