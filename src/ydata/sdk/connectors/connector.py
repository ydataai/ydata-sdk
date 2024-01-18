from json import loads as json_loads
from pathlib import Path
from typing import Dict, Optional, Union
from uuid import uuid4

from ydata.sdk.common.client import Client
from ydata.sdk.common.client.utils import init_client
from ydata.sdk.common.config import LOG_LEVEL
from ydata.sdk.common.exceptions import CredentialTypeError, InvalidConnectorError
from ydata.sdk.common.logger import create_logger
from ydata.sdk.common.types import UID, Project
from ydata.sdk.connectors._models.connector import Connector as mConnector
from ydata.sdk.connectors._models.connector_list import ConnectorsList
from ydata.sdk.connectors._models.connector_type import ConnectorType
from ydata.sdk.connectors._models.credentials.credentials import Credentials
from ydata.sdk.utils.model_mixin import ModelFactoryMixin


class Connector(ModelFactoryMixin):
    """A [`Connector`][ydata.sdk.connectors.Connector] allows to connect and
    access data stored in various places. The list of available connectors can
    be found [here][ydata.sdk.connectors.ConnectorType].

    Arguments:
        connector_type (Union[ConnectorType, str]): Type of the connector to be created
        credentials (dict): Connector credentials
        name (Optional[str]): (optional) Connector name
        project (Optional[Project]): (optional) Project name for this Connector
        client (Client): (optional) Client to connect to the backend

    Attributes:
        uid (UID): UID fo the connector instance (creating internally)
        type (ConnectorType): Type of the connector
    """

    def __init__(
            self, connector_type: Union[ConnectorType, str] = None, credentials: Optional[Dict] = None,
            name: Optional[str] = None, project: Optional[Project] = None, client: Optional[Client] = None):
        self._init_common(client=client)
        self._model: Optional[mConnector] = self._create_model(
            connector_type, credentials, name, client=client)

        self._project = project

    @init_client
    def _init_common(self, client: Optional[Client] = None):
        self._client = client
        self._logger = create_logger(__name__, level=LOG_LEVEL)

    @property
    def uid(self) -> UID:
        return self._model.uid

    @property
    def type(self) -> ConnectorType:
        return self._model.type

    @property
    def project(self) -> Project:
        return self._project or self._client.project

    @staticmethod
    @init_client
    def get(uid: UID, project: Optional[Project] = None, client: Optional[Client] = None) -> "Connector":
        """Get an existing connector.

        Arguments:
            uid (UID): Connector identifier
            project (Optional[Project]): (optional) Project name from where to get the connector
            client (Optional[Client]): (optional) Client to connect to the backend

        Returns:
            Connector
        """
        response = client.get(f'/connector/{uid}', project=project)
        data = response.json()
        connector = Connector._init_from_model_data(Connector, mConnector(**data))
        connector._project = project

        return connector

    @staticmethod
    def _init_connector_type(connector_type: Union[ConnectorType, str]) -> ConnectorType:
        if isinstance(connector_type, str):
            try:
                connector_type = ConnectorType(connector_type)
            except Exception:
                c_list = ", ".join([c.value for c in ConnectorType])
                raise InvalidConnectorError(
                    f"ConnectorType '{connector_type}' does not exist.\nValid connector types are: {c_list}.")
        return connector_type

    @staticmethod
    def _init_credentials(connector_type: ConnectorType, credentials: Union[str, Path, Dict, Credentials]) -> Credentials:
        _credentials = None

        if isinstance(credentials, str):
            credentials = Path(credentials)

        if isinstance(credentials, Path):
            try:
                _credentials = json_loads(credentials.open().read())
            except Exception:
                raise CredentialTypeError(
                    'Could not read the credentials. Please, check your path or credentials structure.')

        try:
            from ydata.sdk.connectors._models.connector_map import TYPE_TO_CLASS
            credential_cls = TYPE_TO_CLASS.get(connector_type.value)
            _credentials = credential_cls(**_credentials)
        except Exception:
            raise CredentialTypeError(
                "Could not create the credentials. Verify the path or the structure your credentials.")

        return _credentials

    @staticmethod
    def create(
        connector_type: Union[ConnectorType, str], credentials: Union[str, Path, Dict, Credentials],
        name: Optional[str] = None, project: Optional[Project] = None, client: Optional[Client] = None
    ) -> "Connector":
        """Create a new connector.

        Arguments:
            connector_type (Union[ConnectorType, str]): Type of the connector to be created
            credentials (dict): Connector credentials
            name (Optional[str]): (optional) Connector name
            project (Optional[Project]): (optional) Project where to create the connector
            client (Client): (optional) Client to connect to the backend

        Returns:
            New connector
        """
        model = Connector._create_model(
            connector_type=connector_type, credentials=credentials, name=name, project=project, client=client)
        connector = ModelFactoryMixin._init_from_model_data(
            Connector, model)
        connector._project = project
        return connector

    @classmethod
    @init_client
    def _create_model(
            cls, connector_type: Union[ConnectorType, str], credentials: Union[str, Path, Dict, Credentials],
            name: Optional[str] = None, project: Optional[Project] = None, client: Optional[Client] = None) -> mConnector:
        _name = name if name is not None else str(uuid4())
        _connector_type = Connector._init_connector_type(connector_type)
        _credentials = Connector._init_credentials(_connector_type, credentials)
        payload = {
            "type": _connector_type.value,
            "credentials": _credentials.dict(by_alias=True),
            "name": _name
        }
        response = client.post('/connector/', project=project, json=payload)
        data: list = response.json()

        return mConnector(**data)

    @staticmethod
    @init_client
    def list(project: Optional[Project] = None, client: Optional[Client] = None) -> ConnectorsList:
        """List the connectors instances.

        Arguments:
            project (Optional[Project]): (optional) Project name from where to list the connectors
            client (Client): (optional) Client to connect to the backend

        Returns:
            List of connectors
        """
        response = client.get('/connector', project=project)
        data: list = response.json()
        return ConnectorsList(data)

    def __repr__(self):
        return self._model.__repr__()
