from dataclasses import dataclass, field

from ydata.sdk.connectors.models.credentials.credentials import Credentials

@dataclass
class AWSS3Credentials(Credentials):
    access_key_id: str
    secret_access_key: str
    region: str = field(default='eu-central-1')

    def asdict(self) -> dict:
        return {
            'keyID': self.access_key_id,
            'keySecret': self.secret_access_key
        }