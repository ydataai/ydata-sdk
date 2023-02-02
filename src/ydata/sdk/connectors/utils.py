from ydata.sdk.connectors.models.credentials.credentials import Credentials

def asdict(credentials: Credentials):
    return credentials.asdict()