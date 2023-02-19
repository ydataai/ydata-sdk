from ydata.sdk.connectors.models.credentials.credentials import Credentials


class BigQueryCredentials(Credentials):
    project_id: str
    private_key_id: str
    private_key: str
    client_email: str
    client_id: str
    token_uri: str
