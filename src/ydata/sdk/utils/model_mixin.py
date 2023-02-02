

class ModelMixin:

    @staticmethod
    def _init_from_model_data(cls, model) -> "cls":
        o = cls()
        o._model = model
        return o