from dataclasses import dataclass, field

from prettytable import PrettyTable
from typeguard import typechecked

from ydata.sdk.utils.list_item_utils import filter_and_assign
from ydata.sdk.utils.table import MISSING_DATE, MISSING_NAME, MISSING_STATUS


@typechecked
class SynthesizersList(list):

    _HEADER = ["Name", "Status", "ID", "Creation Date"]

    _MAP_API_FIELDS = {
        'createdDate': 'creation_date',
        'uid': 'id'
    }

    @dataclass(init=False)
    @filter_and_assign
    class ListItem:
        id: str
        name: str = field(default=MISSING_NAME)
        creation_date: str = field(default=MISSING_DATE)
        status: str = field(init=False)

        def __init__(self, **_):
            self.status = self.status.get('state', MISSING_STATUS)

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self):
        t = PrettyTable(field_names=self._HEADER, align="l")
        for e in self:
            row = self.ListItem(fields_mapping=SynthesizersList._MAP_API_FIELDS, **e)
            t.add_row([row.name, row.status, row.id, row.creation_date])

        return t.get_string()
