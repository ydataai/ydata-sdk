from ydata.sdk.connectors._models.credentials.credentials import Credentials


class GCSCredentials(Credentials):
    project_id: str
    private_key_id: str
    private_key: str
    client_email: str
    client_id: str
    token_uri: str
