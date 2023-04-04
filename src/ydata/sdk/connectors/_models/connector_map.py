from ydata.sdk.connectors._models.connector_type import ConnectorType
from ydata.sdk.connectors._models.credentials.awes3 import AWSS3Credentials
from ydata.sdk.connectors._models.credentials.azureblob import AzureBlobCredentials
from ydata.sdk.connectors._models.credentials.azuresql import AzureSQLCredentials
from ydata.sdk.connectors._models.credentials.bigquery import BigQueryCredentials
from ydata.sdk.connectors._models.credentials.googlecloudstorage import GCSCredentials
from ydata.sdk.connectors._models.credentials.mysql import MySQLCredentials
from ydata.sdk.connectors._models.credentials.postgresql import PostgreSQLCredentials
from ydata.sdk.connectors._models.credentials.snowflake import SnowflakeCredentials

TYPE_TO_CLASS = {
    ConnectorType.GCS.value: GCSCredentials,
    ConnectorType.AWS_S3.value: AWSS3Credentials,
    ConnectorType.AZURE_BLOB.value: AzureBlobCredentials,
    ConnectorType.MYSQL.value: MySQLCredentials,
    ConnectorType.AZURE_SQL.value: AzureSQLCredentials,
    ConnectorType.BIGQUERY.value: BigQueryCredentials,
    ConnectorType.SNOWFLAKE.value: SnowflakeCredentials,
    ConnectorType.POSTGRESQL.value: PostgreSQLCredentials,
}
