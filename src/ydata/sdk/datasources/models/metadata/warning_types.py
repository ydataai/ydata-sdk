from ydata.core.enum import StringEnum

class Level(StringEnum):
    """Warning levels."""

    MODERATE = 1
    HIGH = 2


class WarningType(StringEnum):
    """Warning types."""

    SKEWNESS = "skewness"
    MISSINGS = "missings"
    CARDINALITY = "cardinality"
    DUPLICATES = "duplicates"
    IMBALANCE = "imbalance"
    CONSTANT = "constant"
    INFINITY = "infinity"
    ZEROS = "zeros"
    CORRELATION = "correlation"
    UNIQUE = "unique"
    UNIFORM = "uniform"
    CONSTANT_LENGTH = "constant_length"