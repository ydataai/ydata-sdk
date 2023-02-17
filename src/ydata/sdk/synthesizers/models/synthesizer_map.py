from ydata.sdk.synthesizers.models.synthesizer_type import SynthesizerType
from ydata.sdk.synthesizers.tabular import TabularSynthesizer
from ydata.sdk.synthesizers.timeseries import TimeSeriesSynthesizer

TYPE_TO_CLASS = {
    SynthesizerType.TABULAR.value: TabularSynthesizer,
    SynthesizerType.TIMESERIES.value: TimeSeriesSynthesizer
}
