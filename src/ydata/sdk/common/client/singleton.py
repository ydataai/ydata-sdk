

class SingletonClient(type):
    GLOBAL_CLIENT = None

    def __call__(cls, set_as_global: bool = False, *args, **kwargs):
        if set_as_global:
            cls.GLOBAL_CLIENT = super(SingletonClient, cls).__call__(*args, **kwargs)

        if cls.GLOBAL_CLIENT is not None:
            return cls.GLOBAL_CLIENT
        else:
            return super(SingletonClient, cls).__call__(*args, **kwargs)
