from ydata.sdk.synthesizers.__models.synthesizer_type import SynthesizerType
from ydata.sdk.synthesizers.regular import RegularSynthesizer
from ydata.sdk.synthesizers.timeseries import TimeSeriesSynthesizer

TYPE_TO_CLASS = {
    SynthesizerType.REGULAR.value: RegularSynthesizer,
    SynthesizerType.TIMESERIES.value: TimeSeriesSynthesizer
}
