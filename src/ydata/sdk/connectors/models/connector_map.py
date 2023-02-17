from ydata.sdk.connectors.models.connector_type import ConnectorType
from ydata.sdk.connectors.models.credentials.googlecloudstorage import GCSCredentials
from ydata.sdk.connectors.models.credentials.awes3 import AWSS3Credentials

TYPE_TO_CLASS = {
    ConnectorType.GCS.value: GCSCredentials,
    ConnectorType.AWS_S3.value: AWSS3Credentials
}
