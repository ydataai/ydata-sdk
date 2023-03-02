from typing import List, Union

from pydantic import Field

from ydata.sdk.common.model import BaseModel


class DataSourceAttrs(BaseModel):
    """[`DataSourceAttrs`][ydata.sdk.datasources.DataSourceAttrs] are used to
    configure a [`Synthesizer`][ydata.sdk.synthesizers.Synthesizer] fitting
    process.

    Whenever a [`DataSourceAttrs`][ydata.sdk.datasources.DataSourceAttrs] is required, a `dict` can be provided instead.
    All arguments are optional except `sortbykey` that needs to be provided for [`TimeSeries`][ydata.sdk.datasources.datasource.DataSourceType.TIMESERIES] [`DataSource`][ydata.sdk.datasources.datasource.DataSource].

    By default, if `generate_cols` or `exclude_cols` are not specified, all columns are generated by the synthesizer.
    The argument `exclude_cols` has precedence over `generate_cols`, i.e. a column `col` will not be generated if it is in both list.

    Attributes:
        sortbykey (Union[str, List[str]]): (optional) column(s) to use to sort timeseries datasets
        entity_id_cols (Union[str, List[str]]): (optional) columns representing entities ID
        generate_cols (List[str]): (optional) columns that should be synthesized
        exclude_cols (List[str]): (optional) columns that should not be synthesized
    """
    sortbykey: Union[str, List[str]] = Field(default_factory=list)
    entity_id_cols: Union[str, List[str]] = Field(default_factory=list)
    generate_cols: List[str] = Field(default_factory=list)
    exclude_cols: List[str] = Field(default_factory=list)

    def __init__(self, **fields):
        sortbykey = fields.get("sortbykey")
        if sortbykey is not None and isinstance(sortbykey, str):
            fields['sortbykey'] = [sortbykey]

        entity_id_cols = fields.get("entity_id_cols")
        if entity_id_cols is not None and isinstance(entity_id_cols, str):
            fields['entity_id_cols'] = [entity_id_cols]

        super().__init__(**fields)