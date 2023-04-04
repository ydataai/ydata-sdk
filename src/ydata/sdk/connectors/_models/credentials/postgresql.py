from ydata.sdk.connectors._models.credentials.credentials import Credentials


class PostgreSQLCredentials(Credentials):
    username: str
    password: str
    host: str
    database: str
    port: str
