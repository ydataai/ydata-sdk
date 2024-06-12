from typing import Optional

from pydantic import Field

from ydata.core.enum import StringEnum
from ydata.sdk.common.model import BaseModel
from ydata.sdk.common.status import GenericStateErrorStatus


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

    state: Optional[State] = Field(None)
    prepare: Optional[PrepareStatus] = Field(None)
    training: Optional[TrainingStatus] = Field(None)
    report: Optional[ReportStatus] = Field(None)

    @staticmethod
    def not_initialized() -> "Status":
        return Status(state=Status.State.NOT_INITIALIZED)

    @staticmethod
    def unknown() -> "Status":
        return Status(state=Status.State.UNKNOWN)
