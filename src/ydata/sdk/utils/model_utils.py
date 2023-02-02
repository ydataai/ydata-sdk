from dataclasses import fields


def filter_dict(cls, data):
    mfields = [f.name for f in fields(cls)]
    return {k: v for k, v in data.items() if k in mfields}
