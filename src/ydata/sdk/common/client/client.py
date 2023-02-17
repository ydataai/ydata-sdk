from contextlib import suppress
from typing import Optional, Union

from httpx import Client as httpClient
from httpx import HTTPStatusError, Response
from httpx import codes as http_codes
from typeguard import typechecked

from ydata.sdk.common.client.singleton import SingletonClient
from ydata.sdk.common.exceptions import ResponseError
from ydata.sdk.common.types import Project

codes = http_codes


@typechecked
class Client(metaclass=SingletonClient):
    """Main Client class used to abstract the connection to the backend.

    Args:
        credentials (Optional[dict]): (optional) Credentials to connect
        project (Optional[Project]): (optional) Project to connect to. If not specified, the client will connect to the default user's project.
    """

    codes = codes

    def __init__(self, credentials: Optional[Union[str, dict]] = None, project: Optional[Project] = None, set_as_global: bool = False):
        self._base_url = "fabric.dev.aws.ydata.ai"  # TODO: get from env variable / credentials / whatever
        self._scheme = 'https'
        self._headers = {'Authorization': credentials}
        self._project = 'b0ff40f7-e457-48c6-a0e3-6d755b51c31e'  # project
        self._http_client = httpClient(headers=self._headers)
        self.project = project
        if set_as_global:
            self.__set_global()

    def post(self, endpoint: str, data: Optional[dict] = None, json: Optional[dict] = None, files: Optional[dict] = None, raise_for_status: bool = True) -> Response:
        """POST request to the backend.

        Args:
            endpoint (str): POST endpoint
            data (Optional[Project]): (optional) multipart form data
            json (Optional[dict]): (optional) json data
            files (Optional[dict]): (optional) files to be sent
            raise_for_status (bool): raise an exception on error

        Returns:
            Response object
        """
        url_data = self.__build_url(endpoint, data=data, json=json, files=files)
        response = self._http_client.post(**url_data)

        if response.status_code != Client.codes.OK and raise_for_status:
            self.__raise_for_status(response)

        return response

    def get(self, endpoint: str, raise_for_status=True) -> Response:
        """GET request to the backend.

        Args:
            endpoint (str): GET endpoint
            raise_for_status (bool): raise an exception on error

        Returns:
            Response object
        """
        url_data = self.__build_url(endpoint)
        response = self._http_client.get(**url_data)

        if response.status_code != Client.codes.OK and raise_for_status:
            self.__raise_for_status(response)

        return response

    def get_static_file(self, endpoint: str, raise_for_status: bool = True) -> Response:
        """Retrieve a static file from the backend.

        Args:
            endpoint (str): GET endpoint
            raise_for_status (bool): raise an exception on error

        Returns:
            Response object
        """
        url_data = self.__build_url(endpoint)
        url_data['url'] = f'{self._scheme}://{self._base_url}/static-content{endpoint}'
        response = self._http_client.get(**url_data)

        if response.status_code != Client.codes.OK and raise_for_status:
            self.__raise_for_status(response)

        return response

    def _get_default_project(self):  # TODO: Automatically determine the project based on the token
        response = self.get('/profile')
        return response

    def __build_url(self, endpoint: str, params: Optional[dict] = None, data: Optional[dict] = None, json: Optional[dict] = None, files: Optional[dict] = None) -> dict:
        """Build a request for the backend

        Args:
            endpoint (str): backend endpoint
            params (Optional[dict]): URL parameters
            data (Optional[Project]): (optional) multipart form data
            json (Optional[dict]): (optional) json data
            files (Optional[dict]): (optional) files to be sent

        Returns:
            dictionary containing the information to perform a request
        """
        _params = params if params is not None else {
            'ns': self._project
        }

        url_data = {
            'url': f'{self._scheme}://{self._base_url}/api{endpoint}',
            'headers': self._headers,
            'params': _params,
        }

        if data is not None:
            url_data['data'] = data

        if json is not None:
            url_data['json'] = json

        if files is not None:
            url_data['files'] = files

        return url_data

    def __set_global(self) -> None:
        """Sets a client instance as global
        """
        # If the client is stateful, close it gracefully!
        Client.GLOBAL_CLIENT = self

    def __raise_for_status(self, response: Response) -> None:
        """Raise an exception if the response is not OK

        When an exception is raised, we try to convert it to a ResponseError which is
        a wrapper around a backend error. This usually gives enough context and provides
        nice error message.

        If it cannot be converted to ResponseError, it is re-raised.

        Args:
            response (Response): response to analyze
        """
        try:
            response.raise_for_status()
        except HTTPStatusError as e:
            with suppress(Exception):
                e = ResponseError(**response.json())
            raise e
