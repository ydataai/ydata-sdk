import json
from contextlib import suppress
from functools import wraps
from os import environ
from pathlib import Path
from typing import Optional, Union

from ydata.sdk.common.client.client import Client
from ydata.sdk.common.exceptions import ClientCreationError


def get_client(client_or_creds: Optional[Union[Client, dict, str, Path]] = None, set_as_global: bool = False) -> Client:
    """Deduce how to initialize or retrieve the client.

    This is meant to be a zero configuration for the user.
    """
    # If a client instance is set globally, return it
    if not set_as_global and Client.GLOBAL_CLIENT is not None:
        return Client.GLOBAL_CLIENT

    # Client exists, forward it
    if isinstance(client_or_creds, Client):
        return client_or_creds

    # Explicit credentials
    if isinstance(client_or_creds, (dict, str, Path)):
        if isinstance(client_or_creds, str):  # noqa: SIM102
            if Path(client_or_creds).is_file():
                client_or_creds = Path(client_or_creds)

        if isinstance(client_or_creds, Path):
            # TODO: Check that the file exists
            client_or_creds = json.loads(client_or_creds.open().read())

        return Client(credentials=client_or_creds)

    # Last try with environment variables
    if client_or_creds is None:
        client = _client_from_env()

        if client is None:
            raise ClientCreationError("Could not initialize a client")

        return client


def _client_from_env(env_var: str = 'YDATA_CREDENTIALS') -> Optional[Client]:
    """Deduce how to initialize a client from environment variable.

    If the environment variable is not defined, the return is None. It
    is on the caller to check the return.
    """
    credentials = environ.get(env_var)
    if credentials is not None:
        # Try to load it as a dictionary. If it fails, consider it as str/path to a file
        with suppress(Exception):
            credentials = json.loads(credentials)
        return get_client(client_or_creds=credentials, set_as_global=True)


def require_client(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        if not any((arg for arg in args if isinstance(arg, Client))):
            kwargs['client'] = get_client(kwargs.get('client'))
        return func(*args, **kwargs)
    return wrapper_func
