from typing import Dict, List, Optional, Union

from pandas import DataFrame as pdDataFrame

from ydata.sdk.common.exceptions import InputError
from ydata.sdk.datasources import DataSource
from ydata.sdk.datasources._models.datatype import DataSourceType
from ydata.sdk.datasources._models.metadata.data_types import DataType
from ydata.core.enum import PrivacyLevel
from ydata.sdk.synthesizers.synthesizer import BaseSynthesizer


class RegularSynthesizer(BaseSynthesizer):

    def sample(self, n_samples: int = 1) -> pdDataFrame:
        """Sample from a [`RegularSynthesizer`][ydata.sdk.synthesizers.RegularSynthesizer]
        instance.

        Arguments:
            n_samples (int): number of rows in the sample

        Returns:
            synthetic data
        """
        if n_samples < 1:
            raise InputError("Parameter 'n_samples' must be greater than 0")

        return self._sample(payload={"numberOfRecords": n_samples})

    def fit(self, X: Union[DataSource, pdDataFrame],
            privacy_level: PrivacyLevel = PrivacyLevel.HIGH_FIDELITY,
            entity_id_cols: Optional[Union[str, List[str]]] = None,
            generate_cols: Optional[List[str]] = None,
            exclude_cols: Optional[List[str]] = None,
            dtypes: Optional[Dict[str, Union[str, DataType]]] = None,
            target: Optional[str] = None,
            name: Optional[str] = None,
            anonymize: Optional[dict] = None) -> None:
        """Fit the synthesizer.

        The synthesizer accepts as training dataset either a pandas [`DataFrame`][pandas.DataFrame] directly or a YData [`DataSource`][ydata.sdk.datasources.DataSource].

        Arguments:
            X (Union[DataSource, pandas.DataFrame]): Training dataset
            privacy_level (PrivacyLevel): Synthesizer privacy level (defaults to high fidelity)
            entity_id_cols (Union[str, List[str]]): (optional) columns representing entities ID
            generate_cols (List[str]): (optional) columns that should be synthesized
            exclude_cols (List[str]): (optional) columns that should not be synthesized
            dtypes (Dict[str, Union[str, DataType]]): (optional) datatype mapping that will overwrite the datasource metadata column datatypes
            target (Optional[str]): (optional) Target column
            name (Optional[str]): (optional) Synthesizer instance name
            anonymize (Optional[str]): (optional) fields to anonymize and the anonymization strategy
        """
        BaseSynthesizer.fit(self, X=X, datatype=DataSourceType.TABULAR, entity_id_cols=entity_id_cols,
                            generate_cols=generate_cols, exclude_cols=exclude_cols, dtypes=dtypes,
                            target=target, name=name, anonymize=anonymize, privacy_level=privacy_level)

    def __repr__(self):
        if self._model is not None:
            return self._model.__repr__()
        else:
            return "RegularSynthesizer(Not Initialized)"
