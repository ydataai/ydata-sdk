from typing import Optional, Union

from pandas import DataFrame as pdDataFrame

from ydata.sdk.common.exceptions import InputError
from ydata.sdk.datasources import DataSource
from ydata.sdk.datasources._models.attributes import DataSourceAttrs
from ydata.sdk.datasources._models.datatype import DataSourceType
from ydata.sdk.synthesizers.synthesizer import BaseSynthesizer


class RegularSynthesizer(BaseSynthesizer):

    def sample(self, n_samples: int = 1) -> pdDataFrame:
        """Sample from a.

        [`RegularSynthesizer`][ydata.sdk.synthesizers.RegularSynthesizer]
        instance.

        Arguments:
            n_samples (int): number of rows in the sample

        Returns:
            synthetic data
        """
        if n_samples < 1:
            raise InputError("Parameter 'n_samples' must be greater than 0")

        return self._sample(payload={"numberOfRecords": n_samples})

    def fit(self, X: Union[DataSource, pdDataFrame], dataset_attrs: Optional[DataSourceAttrs] = None, target: Optional[str] = None, name: Optional[str] = None) -> None:
        """Fit the synthesizer.

        The synthesizer accepts as training dataset either a pandas [`DataFrame`][pandas.DataFrame] directly or a YData [`DataSource`][ydata.sdk.datasources.DataSource].

        Arguments:
            X (Union[DataSource, pandas.DataFrame]): Training dataset
            dataset_attrs (Optional[Union[DataSourceAttrs, dict]]): (optional) Dataset attributes
            target (Optional[str]): (optional) Metadata associated to the datasource
            name (Optional[str]): (optional) Synthesizer instance name
        """
        BaseSynthesizer.fit(self, X=X, datatype=DataSourceType.TABULAR,
                            dataset_attrs=dataset_attrs, target=target, name=name)

    def __repr__(self):
        if self._model is not None:
            return self._model.__repr__()
        else:
            return "RegularSynthesizer(Not Initialized)"
