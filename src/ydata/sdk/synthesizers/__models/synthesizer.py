from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Synthesizer:

    uid: Optional[str] = None
    author: Optional[str] = None
    name: Optional[str] = None
    metadata: Optional[dict] = field(default_factory=dict)  # TODO METADATA OBJECT
    report: Optional[dict] = field(default_factory=dict)
    status: Optional[dict] = field(default_factory=dict)
