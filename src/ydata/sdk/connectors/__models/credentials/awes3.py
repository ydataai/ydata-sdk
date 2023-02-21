from pydantic import Field

from ydata.sdk.connectors.__models.credentials.credentials import Credentials


class AWSS3Credentials(Credentials):
    access_key_id: str
    secret_access_key: str
    region: str = Field(default='eu-central-1')

    def as_payload(self) -> dict:
        return {
            'keyID': self.access_key_id,
            'keySecret': self.secret_access_key
        }
