from typing import Optional

from pandas import DataFrame as pdDataFrame

from ydata.sdk.synthesizers.synthesizer import BaseSynthesizer
from ydata.sdk.common.exceptions import InputError


class RegularSynthesizer(BaseSynthesizer):

    def sample(self, n_samples: int = 1, anonymize: Optional[dict] = None) -> pdDataFrame:
        if n_samples < 1:
            raise InputError("Parameter 'n_samples' must be greater than 0")
        
        return self._sample(payload={"numberOfRecords": n_samples})
