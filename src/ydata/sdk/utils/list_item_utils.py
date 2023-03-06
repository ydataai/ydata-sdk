from dataclasses import fields


def filter_and_assign(cls):
    _init = cls.__init__

    def __init__(self, fields_mapping, **kwargs):
        fields_mapping = fields_mapping if fields_mapping is not None else {}
        names = set([f.name for f in fields(self)])
        for k, v in kwargs.items():
            fname = fields_mapping.get(k, k)
            if fname in names:
                setattr(self, fname, v)
        _init(self)

    cls.__init__ = __init__
    return cls
