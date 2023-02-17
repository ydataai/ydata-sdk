from typing import Optional, Union

from pandas import DataFrame as pdDataFrame

from ydata.sdk.synthesizers.synthesizer import BaseSynthesizer
from ydata.sdk.common.exceptions import InputError
from ydata.sdk.datasources.models.datatype import DataSourceType
from ydata.sdk.datasources import DataSource

Metadata = dict  # TODO
class TimeSeriesSynthesizer(BaseSynthesizer):

    def sample(self, n_entities: Optional[int] = None) -> pdDataFrame:
        if n_entities is not None and n_entities < 1:
            raise InputError("Parameter 'n_samples' must be greater than 0")
        
        return self._sample(payload={"numberOfRecords": n_entities})

    def fit(self, X: Union[DataSource, pdDataFrame], metadata: Optional[Metadata] = None, target: Optional[str] = None, name: Optional[str] = None) -> None:
        BaseSynthesizer.fit(self, X=X, datatype=DataSourceType.TIMESERIES, metadata=metadata, target=target, name=name)