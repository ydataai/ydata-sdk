from ydata.sdk.connectors.__models.credentials.credentials import Credentials


class MySQLCredentials(Credentials):
    username: str
    password: str
    host: str
    port: str
