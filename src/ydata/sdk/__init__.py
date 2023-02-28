from pathlib import Path
from warnings import warn

from ydata.sdk.common.client.client import HELP_TEXT
from ydata.sdk.common.warnings import NewUserWarning

source_root = Path(".")

try:
    __version__ = (source_root / "VERSION").read_text().rstrip("\n")
except FileNotFoundError:
    __version__ = "0.0.dev0"


warn(HELP_TEXT, NewUserWarning)
