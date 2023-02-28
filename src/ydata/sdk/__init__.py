from os import environ
from pathlib import Path
from warnings import warn

from ydata.sdk.common.client.client import HELP_TEXT
from ydata.sdk.common.config import TOKEN_VAR
from ydata.sdk.common.warnings import NewUserWarning

source_root = Path(".")

try:
    __version__ = (source_root / "VERSION").read_text().rstrip("\n")
except FileNotFoundError:
    __version__ = "0.0.dev0"

token = environ.get(TOKEN_VAR)
if token is None:
    warn(HELP_TEXT, NewUserWarning)
