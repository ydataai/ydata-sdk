
from dataclasses import dataclass, field, fields
from typing import Any, Optional, Union

from prettytable import PrettyTable
from typeguard import typechecked

from ydata.sdk.utils.table import MISSING_COUNT, MISSING_DATE, MISSING_NAME
from ydata.sdk.utils.list_item_utils import filter_and_assign

@typechecked
class ConnectorsList(list):

    _HEADER = ["Name", "Type", "# Datasources", "UID", "Creation Date"]

    _MAP_API_FIELDS = {
        'createdDate': 'creation_date',
        'numberOfDataSources': 'datasources_count',
    }

    @dataclass(init=False)
    @filter_and_assign
    class ListItem:
        uid: str
        type: str
        name: str = field(default=MISSING_NAME)
        creation_date: str = field(default=MISSING_DATE)
        status: str = field(init=False)
        datasources_count: Union[int, str] = MISSING_COUNT

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self):
        t = PrettyTable(field_names=self._HEADER, align="l")
        t.align["# Datasources"] = 'r'
        for e in self:
            row = self.ListItem(fields_mapping=ConnectorsList._MAP_API_FIELDS, **e)
            t.add_row([row.name, row.type, row.datasources_count,
                      row.uid, row.creation_date])

        return t.get_string()

    def get_by_name(self, name: str, default: Optional[Any] = 'raise') -> Union[dict, Any]:
        args = [(c for c in self if c['name'] == name), default]
        return next(*args[:1 if default == 'raise' else 2])

    def get_by_uid(self, uid: str, default: Optional[Any] = 'raise') -> Union[dict, Any]:
        args = [(c for c in self if c['uid'] == uid), default]
        return next(*args[:1 if default == 'raise' else 2])
