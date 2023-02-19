from ydata.sdk.connectors.models.credentials.credentials import Credentials


class AzureSQLCredentials(Credentials):
    username: str
    password: str
    server: str
    database_name: str
