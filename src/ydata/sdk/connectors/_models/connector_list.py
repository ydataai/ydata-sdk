
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Union

from prettytable import PrettyTable
from typeguard import typechecked

from ydata.sdk.utils.list_item_utils import filter_and_assign
from ydata.sdk.utils.table import MISSING_COUNT, MISSING_DATE, MISSING_NAME


@typechecked
class ConnectorsList(list):
    """Representation of the list of `Connectors` objects.

    The list inherits directly from Python `list`. The list does not
    communicate with the backend and thus, represent a snapshot at the
    moment it is created.
    """

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

    def get_by_name(self, name: str, default: Optional[Any] = 'raise') -> Union[Dict, Any]:
        args = [(c for c in self if c['name'] == name), default]
        return next(*args[:1 if default == 'raise' else 2])

    def get_by_uid(self, uid: str, default: Optional[Any] = 'raise') -> Union[Dict, Any]:
        args = [(c for c in self if c['uid'] == uid), default]
        return next(*args[:1 if default == 'raise' else 2])
