import json
from contextlib import suppress
from functools import wraps
from os import environ
from pathlib import Path
from time import sleep, time
from typing import Optional, Union

from ydata.sdk.common.client.client import Client
from ydata.sdk.common.config import BACKOFF
from ydata.sdk.common.exceptions import ClientCreationError, ClientHandshakeError

CLIENT_INIT_TIMEOUT = 5 * 60  # 5 min
WAITING_FOR_CLIENT = False


def get_client(client_or_creds: Optional[Union[Client, dict, str, Path]] = None, set_as_global: bool = False, wait_for_auth: bool = True) -> Client:
    """Deduce how to initialize or retrieve the client.

    This is meant to be a zero configuration for the user.

    Example: Create and set a client globally
            ```py
            from ydata.sdk.client import get_client
            get_client(set_as_global=True)
            ```

    Args:
        client_or_creds (Optional[Union[Client, dict, str, Path]]): Client to forward or credentials for initialization
        set_as_global (bool): If `True`, set client as global
        wait_for_auth (bool): If `True`, wait for the user to authenticate

    Returns:
        Client instance
    """
    client = None
    global WAITING_FOR_CLIENT
    try:

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
                client_or_creds = json.loads(client_or_creds.open().read())

            return Client(credentials=client_or_creds)

        # Last try with environment variables
        if client_or_creds is None:
            client = _client_from_env(wait_for_auth=wait_for_auth)

    except ClientHandshakeError as e:
        wait_for_auth = False  # For now deactivate wait_for_auth until the backend is ready
        if wait_for_auth:
            WAITING_FOR_CLIENT = True
            start = time()
            login_message_printed = False
            while client is None:
                if not login_message_printed:
                    print(
                        f"The token needs to be refreshed - please validate your token by browsing at the following URL:\n\n\t{e.auth_link}")
                    login_message_printed = True
                with suppress(ClientCreationError):
                    sleep(BACKOFF)
                    client = get_client(wait_for_auth=False)
                now = time()
                if now - start > CLIENT_INIT_TIMEOUT:
                    WAITING_FOR_CLIENT = False
                    break
    except Exception as e:
        raise ClientCreationError(
            f"Could not initialize a client due to the following error:\n{str(e)}")

    if client is None and not WAITING_FOR_CLIENT:
        raise ClientCreationError("Could not initialize a client. It usually means that no token or credential files could be found.\n\n\
        The easiest way to have the client created is to define the token in an environment variable 'YDATA_CREDENTIALS'.\n\n\
        See the documentation for further help.")  # TODO: Adjust the link for the documentation
    return client


def _client_from_env(env_var: str = 'YDATA_CREDENTIALS', wait_for_auth: bool = True) -> Optional[Client]:
    """Deduce how to initialize a client from environment variable.

    If the environment variable is not defined, the return is None. It
    is on the caller to check the return.

    Args:
        env_var (str): name of the environment variable to look for
        wait_for_auth (bool): if True, wait for the user authentication if the token needs to be refreshed

    Returns:
        client instance or None if there is no environment variable
    """
    credentials = environ.get(env_var)
    if credentials is not None:
        # Try to load it as a dictionary. If it fails, consider it as str/path to a file
        with suppress(Exception):
            credentials = json.loads(credentials)
        return get_client(client_or_creds=credentials, set_as_global=True, wait_for_auth=wait_for_auth)


def init_client(func):
    """Decorator to intialize a client automatically.

    It intercept a client object in the decorated functionc all and wrap
    it with `get_client` function.
    """
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        if not any((arg for arg in args if isinstance(arg, Client))):
            kwargs['client'] = get_client(kwargs.get('client'))
        return func(*args, **kwargs)
    return wrapper_func
