from dataclasses import dataclass, field

from ydata.sdk.connectors.models.credentials.credentials import Credentials

@dataclass
class GCSCredentials(Credentials):
  project_id: str
  private_key_id: str
  private_key: str
  client_email: str
  client_id: str
  token_uri: str
