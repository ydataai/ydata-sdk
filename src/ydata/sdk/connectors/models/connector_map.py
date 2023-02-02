from ydata.sdk.connectors.models.connector_type import ConnectorType
from ydata.sdk.connectors.models.credentials.googlecloudstorage import GCSConnectorCredentials
from ydata.sdk.connectors.models.credentials.awes3 import AWSS3Credentials
#from ydata.sdk.connectors.models.credentials.file import FileCredentials

TYPE_TO_CLASS = {
    #ConnectorType.FILE.value: FileCredentials,
    ConnectorType.GCS.value: GCSConnectorCredentials,
    ConnectorType.AWS_S3.value: AWSS3Credentials
}
