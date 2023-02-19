
from ydata.sdk.connectors.models.credentials.credentials import Credentials


class AzureBlobCredentials(Credentials):
    access_key_id: str
    account_key: str

    def as_payload(self) -> dict:
        return {
            'accountKey': self.access_key_id,
            'accountName': self.account_key
        }
