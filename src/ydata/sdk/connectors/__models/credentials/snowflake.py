from ydata.sdk.connectors.__models.credentials.credentials import Credentials


class SnowflakeCredentials(Credentials):
    username: str
    password: str
    server: str
    database_name: str
    warehouse: str
