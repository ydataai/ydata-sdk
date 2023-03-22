from enum import Enum, auto


class PrivacyLevel(Enum):
    """Privacy level exposed to the end-user."""
    HIGH_FIDELITY = auto()
    HIGH_PRIVACY = auto()
    BALANCED_PRIVACY_FIDELITY = auto()
