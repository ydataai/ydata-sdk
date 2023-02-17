

class ModelMixin:

    @staticmethod
    def _init_from_model_data(cls, model) -> "cls":
        o = cls.__new__(cls)
        o._model = model
        o._init_common()  # TODO: forward client
        return o

    def _init_common(self, *args, **kwargs):
        pass