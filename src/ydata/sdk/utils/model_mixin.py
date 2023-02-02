from typing import Any, Optional, Type

from ydata.sdk.common.client.client import Client
from ydata.sdk.common.model import BaseModel


class ModelFactoryMixin:
    """Mixin for class that implements an interface for an internal model.
    """

    @staticmethod
    def _init_from_model_data(cls: Type, model: BaseModel, client: Optional[Client] = None) -> Any:
        o = cls.__new__(cls)
        o._model = model
        o._init_common(client=client)
        return o

    def _init_common(self, *args, **kwargs):
        pass
