from typing import Optional, Union
from uuid import uuid4
from pathlib import Path
from json import loads as json_loads

from ydata.sdk.common.client import Client, get_client
from ydata.sdk.common.config import LOG_LEVEL
from ydata.sdk.common.logger import create_logger
from ydata.sdk.common.types import UID
from ydata.sdk.common.exceptions import InvalidConnectorError, CredentialTypeError
from ydata.sdk.connectors.models.connector import Connector as mConnector
from ydata.sdk.connectors.models.credentials.credentials import Credentials
from ydata.sdk.connectors.utils import asdict
from ydata.sdk.connectors.models.connector_list import ConnectorsList
from ydata.sdk.connectors.models.connector_type import ConnectorType
from ydata.sdk.utils.model_utils import filter_dict
from ydata.sdk.utils.model_mixin import ModelMixin


class Connector(ModelMixin):

    def __init__(self, connector_type: Optional[Union[ConnectorType, str]] = None, credentials: Optional[dict] = None, client: Optional[Client] = None):
        self._client = get_client(client)
        self._logger = create_logger(__name__, level=LOG_LEVEL)
        self._model: Optional[mConnector] = None

    @property
    def uid(self) -> str:
        return self._model.uid

    @property
    def type(self) -> str:
        return self._model.type

    @staticmethod
    def get(uid: UID, client: Optional[Client] = None) -> "Connector":
        _client = get_client(client)
        connectors: ConnectorsList = Connector.list(client=_client)
        data = connectors.get_by_uid(uid)
        model = Connector._model_from_api(data)
        connector = ModelMixin._init_from_model_data(Connector, model)
        return connector


    @staticmethod
    def _init_connector_type(connector_type: Union[ConnectorType, str]) -> ConnectorType:
        if isinstance(connector_type, str):
            try:
                connector_type =  ConnectorType(connector_type)
            except:
                c_list = ", ".join([c.value for c in ConnectorType])
                raise InvalidConnectorError(f"ConnectorType '{connector_type}' does not exist.\nValid connector types are: {c_list}.")
        return connector_type


    @staticmethod
    def _init_credentials(connector_type: ConnectorType, credentials: Union[str, Path, dict, Credentials]) -> Credentials:
        _credentials = None

        if isinstance(credentials, str):
            credentials = Path(credentials)
        
        if isinstance(credentials, Path):
            try:
                _credentials = json_loads(credentials.open().read())
            except Exception as e:
                pass  # TODO: Catch and re-raise
        
        try:
            from ydata.sdk.connectors.models.connector_map import TYPE_TO_CLASS
            credential_cls =  TYPE_TO_CLASS.get(connector_type.value)
            _credentials = filter_dict(credential_cls, _credentials)
            _credentials = credential_cls(**_credentials)
        except:  # TODO
            raise CredentialTypeError("Could not create the credentials. Verify the path or the structure your credentials.")

        return _credentials


    @staticmethod
    def create(connector_type: Union[ConnectorType, str], credentials: Union[str, Path, dict, Credentials], name: Optional[str] = None, client: Optional[Client] = None) -> "Connector":
        _client = get_client(client)
        _name = name if name is not None else str(uuid4())
        _connector_type = Connector._init_connector_type(connector_type)
        _credentials = Connector._init_credentials(_connector_type, credentials)
        payload = {
            "type": _connector_type.value,
            "credentials": asdict(_credentials),
            "name": _name
        }
        response = _client.post(f'/connector/', json=payload)
        data: list = response.json()
        
        model = Connector._model_from_api(data)
        connector = ModelMixin._init_from_model_data(Connector, model)  # TODO: Return specific class

        return connector

    def list_datasource(self):
        # TODO
        pass

    @staticmethod
    def list(client: Optional[Client] = None) -> ConnectorsList:
        """List the connectors instances.

        Arguments:
            client (Client): (optional) Client to connet to the backend
        """
        _client = get_client(client)
        response = _client.get('/connector')

        # Analyze response and create ConnectorList
        data: list = response.json()

        return ConnectorsList(data)

    @staticmethod
    def _model_from_api(data: dict) -> mConnector:
        connector_cls = mConnector
        data = filter_dict(connector_cls, data)
        model = connector_cls(**data)
        return model

