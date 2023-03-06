from pydantic import Field

from ydata.sdk.connectors._models.credentials.credentials import Credentials


class AWSS3Credentials(Credentials):
    access_key_id: str = Field(alias='keyID')
    secret_access_key: str = Field(alias='keySecret')
    region: str = Field(default='eu-central-1')
