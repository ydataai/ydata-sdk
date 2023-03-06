from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class Synthesizer:

    uid: Optional[str] = None
    author: Optional[str] = None
    name: Optional[str] = None
    status: Optional[Dict] = field(default_factory=dict)
