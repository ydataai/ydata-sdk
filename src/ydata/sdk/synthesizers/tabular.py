from typing import Optional, Union

from pandas import DataFrame as pdDataFrame

from ydata.sdk.common.exceptions import InputError
from ydata.sdk.datasources import DataSource
from ydata.sdk.datasources.models.attributes import DataSourceAttrs
from ydata.sdk.datasources.models.datatype import DataSourceType
from ydata.sdk.synthesizers.synthesizer import BaseSynthesizer

Metadata = dict  # TODO


class TabularSynthesizer(BaseSynthesizer):

    def sample(self, n_samples: int = 1, anonymize: Optional[dict] = None) -> pdDataFrame:
        if n_samples < 1:
            raise InputError("Parameter 'n_samples' must be greater than 0")

        return self._sample(payload={"numberOfRecords": n_samples})

    def fit(self, X: Union[DataSource, pdDataFrame], dataset_attrs: Optional[DataSourceAttrs] = None, target: Optional[str] = None, name: Optional[str] = None) -> None:
        BaseSynthesizer.fit(self, X=X, datatype=DataSourceType.TABULAR,
                            dataset_attrs=dataset_attrs, target=target, name=name)
