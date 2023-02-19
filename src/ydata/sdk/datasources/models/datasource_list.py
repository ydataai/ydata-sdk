from dataclasses import dataclass, field

from prettytable import PrettyTable
from typeguard import typechecked

from ydata.sdk.utils.list_item_utils import filter_and_assign
from ydata.sdk.utils.table import MISSING_CONNECTOR_UID, MISSING_DATATYPE, MISSING_DATE, MISSING_NAME, MISSING_STATUS


@typechecked
class DataSourceList(list):

    _HEADER = ["Name", "Datatype", "Status", "UID", "Connector UID", "Creation Date"]

    _MAP_API_FIELDS = {
        'createdDate': 'creation_date',
        'connector': 'connector_uid',
        'dataType': 'datatype'
    }

    @dataclass(init=False)
    @filter_and_assign
    class ListItem:
        uid: str
        name: str = field(default=MISSING_NAME)
        datatype: str = field(default=MISSING_DATATYPE)
        creation_date: str = field(default=MISSING_DATE)
        status: str = field(init=False)
        connector_uid: str = field(init=False)

        def __init__(self, **_):
            self.status = self.status.get('state', MISSING_STATUS)
            self.connector_uid = self.connector_uid.get('uid', MISSING_CONNECTOR_UID)

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self):
        t = PrettyTable(field_names=self._HEADER, align="l")
        for e in self:
            row = self.ListItem(fields_mapping=DataSourceList._MAP_API_FIELDS, **e)
            t.add_row([row.name, row.datatype, row.status, row.uid,
                      row.connector_uid, row.creation_date])

        return t.get_string()
