from ydata.sdk.synthesizers._models.synthesizer_type import SynthesizerType
from ydata.sdk.synthesizers.regular import RegularSynthesizer
from ydata.sdk.synthesizers.timeseries import TimeSeriesSynthesizer

TYPE_TO_CLASS = {
    SynthesizerType.TABULAR.value: RegularSynthesizer,
    SynthesizerType.TIMESERIES.value: TimeSeriesSynthesizer
}
