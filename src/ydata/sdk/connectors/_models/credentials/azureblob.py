
from pydantic import Field

from ydata.sdk.connectors._models.credentials.credentials import Credentials


class AzureBlobCredentials(Credentials):
    access_key_id: str = Field(alias='accountName')
    account_key: str = Field(alias='accoaccountKeyuntName')
