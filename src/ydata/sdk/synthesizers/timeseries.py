from typing import Optional, Union

from pandas import DataFrame as pdDataFrame

from ydata.sdk.common.exceptions import InputError
from ydata.sdk.datasources import DataSource
from ydata.sdk.datasources._models.attributes import DataSourceAttrs
from ydata.sdk.datasources._models.datatype import DataSourceType
from ydata.sdk.synthesizers.synthesizer import BaseSynthesizer


class TimeSeriesSynthesizer(BaseSynthesizer):

    def sample(self, n_entities: Optional[int] = None) -> pdDataFrame:
        """Sample from a [`TimeSeriesSynthesizer`][ydata.sdk.synthesizers.TimeS
        eriesSynthesizer] instance.

        If a training dataset was not using any `entity` column, the Synthesizer assumes a single entity.
        A [`TimeSeriesSynthesizer`][ydata.sdk.synthesizers.TimeSeriesSynthesizer] always sample the full trajectory of its entities.

        Arguments:
            n_entities (int): (optional) number of entities to sample. If `None`, uses the same number of entities as in the original dataset.

        Returns:
            synthetic data
        """
        if n_entities is not None and n_entities < 1:
            raise InputError("Parameter 'n_samples' must be greater than 0")

        return self._sample(payload={"numberOfRecords": n_entities})

    def fit(self, X: Union[DataSource, pdDataFrame], dataset_attrs: DataSourceAttrs, target: Optional[str] = None, name: Optional[str] = None) -> None:
        """Fit the synthesizer.

        The synthesizer accepts as training dataset either a pandas [`DataFrame`][pandas.DataFrame] directly or a YData [`DataSource`][ydata.sdk.datasources.DataSource].

        Similarly, `dataset_attrs` is mandatory for [`TimeSeries`][ydata.sdk.datasources.DataSourceType.TIMESERIES] dataset to specify the `sortbykey` columns.

        Arguments:
            X (Union[DataSource, pandas.DataFrame]): Training dataset
            dataset_attrs (Union[DataSourceAttrs, dict]): Dataset attributes
            target (Optional[str]): (optional) Metadata associated to the datasource
            name (Optional[str]): (optional) Synthesizer instance name
        """
        BaseSynthesizer.fit(self, X=X, datatype=DataSourceType.TIMESERIES,
                            dataset_attrs=dataset_attrs, target=target, name=name)
