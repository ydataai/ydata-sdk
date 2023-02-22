from ydata.sdk.connectors._models.credentials.credentials import Credentials


class MySQLCredentials(Credentials):
    username: str
    password: str
    host: str
    port: str
