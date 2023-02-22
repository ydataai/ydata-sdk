from ydata.sdk.connectors._models.connector_type import ConnectorType
from ydata.sdk.datasources._models.datasource import DataSource
from ydata.sdk.datasources._models.datasources.aws3 import AWSS3DataSource
from ydata.sdk.datasources._models.datasources.azureblob import AzureBlobDataSource
from ydata.sdk.datasources._models.datasources.azuresql import AzureSQLDataSource
from ydata.sdk.datasources._models.datasources.bigquery import BigQueryDataSource
from ydata.sdk.datasources._models.datasources.googlecloudstorage import GCSDataSource
from ydata.sdk.datasources._models.datasources.mysql import MySQLDataSource

CONN_TO_DS = {
    ConnectorType.GCS: GCSDataSource,
    ConnectorType.AWS_S3: AWSS3DataSource,
    ConnectorType.AZURE_BLOB: AzureBlobDataSource,
    ConnectorType.MYSQL: MySQLDataSource,
    ConnectorType.AZURE_SQL: AzureSQLDataSource,
    ConnectorType.BIGQUERY: BigQueryDataSource,
    ConnectorType.FILE: DataSource
}
