
from enum import Enum


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
    POSTGRESQL = "postgresql"
    """PostgreSQL connector"""
