from typing import Optional

from pandas import DataFrame as pdDataFrame

from ydata.sdk.synthesizers.synthesizer import BaseSynthesizer
from ydata.sdk.common.exceptions import InputError
from ydata.sdk.synthesizers.synthesizer import BaseSynthesizer


class TimeSeriesSynthesizer(BaseSynthesizer):

    def sample(self, n_entities: Optional[int] = None) -> pdDataFrame:
        if n_entities is not None and n_entities < 1:
            raise InputError("Parameter 'n_samples' must be greater than 0")
        
        return self._sample(payload={"numberOfRecords": n_entities})

