
from enum import Enum
from typing import Union

from ydata.sdk.common.exceptions import InvalidConnectorError


class ConnectorType(Enum):
    AWS_S3 = "aws-s3"
    """AWS S3 connector"""
    AZURE_BLOB = "azure-blob"
    """Azure Blob connector"""
    GCS = "gcs"
    """Google Cloud Storage connector"""
    FILE = "file"
    """File connector (placeholder)"""
    MYSQL = "mysql"
    """MySQL connector"""
    AZURE_SQL = "azure-sql"
    """AzureSQL connector"""
    BIGQUERY = "google-bigquery"
    """BigQuery connector"""
    SNOWFLAKE = "snowflake"
    """Snowflake connector"""

    @property
    def is_rdbms(self) -> bool:
        return self in [ConnectorType.AZURE_SQL, ConnectorType.MYSQL, ConnectorType.BIGQUERY, ConnectorType.SNOWFLAKE]

    @staticmethod
    def _init_connector_type(connector_type: Union["ConnectorType", str]) -> "ConnectorType":
        if isinstance(connector_type, str):
            try:
                connector_type = ConnectorType(connector_type)
            except Exception:
                c_list = ", ".join([c.value for c in ConnectorType])
                raise InvalidConnectorError(
                    f"ConnectorType '{connector_type}' does not exist.\nValid connector types are: {c_list}.")
        return connector_type
