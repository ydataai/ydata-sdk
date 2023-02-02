
from os import environ
from warnings import warn

from ydata.sdk.common.client.client import HELP_TEXT
from ydata.sdk.common.config import TOKEN_VAR
from ydata.sdk.common.warnings import NewUserWarning

token = environ.get(TOKEN_VAR)
if token is None:
    warn(HELP_TEXT, NewUserWarning)
