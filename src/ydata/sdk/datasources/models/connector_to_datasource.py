from ydata.sdk.connectors.models.connector_type import ConnectorType
from ydata.sdk.datasources.models.datasource import DataSource
from ydata.sdk.datasources.models.datasources.aws3 import AWSS3DataSource
from ydata.sdk.datasources.models.datasources.azureblob import AzureBlobDataSource
from ydata.sdk.datasources.models.datasources.azuresql import AzureSQLDataSource
from ydata.sdk.datasources.models.datasources.bigquery import BigQueryDataSource
from ydata.sdk.datasources.models.datasources.googlecloudstorage import GCSDataSource
from ydata.sdk.datasources.models.datasources.mysql import MySQLDataSource

CONN_TO_DS = {
    ConnectorType.GCS: GCSDataSource,
    ConnectorType.AWS_S3: AWSS3DataSource,
    ConnectorType.AZURE_BLOB: AzureBlobDataSource,
    ConnectorType.MYSQL: MySQLDataSource,
    ConnectorType.AZURE_SQL: AzureSQLDataSource,
    ConnectorType.BIGQUERY: BigQueryDataSource,
    ConnectorType.FILE: DataSource
}
