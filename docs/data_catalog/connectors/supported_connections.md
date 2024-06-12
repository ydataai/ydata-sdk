# Supported connections

Fabric can read and write data from a variety of data sources.

## Connectors

Here is the list of the available connectors in Fabric.

| Connector Name           |      Type      |                 Supported file types | Notes                                                                                                      |
|:-------------------------|:--------------:|-------------------------------------:|:-----------------------------------------------------------------------------------------------------------|
| AWS S3                   | Object Storage |                      `Parquet` `CSV` |                                                                                                            |
| Azure Blog Storage       | Object Storage |                      `Parquet` `CSV` |                                                                                                            |
| Azure Data Lake          | Object Storage |                      `Parquet` `CSV` |                                                                                                            |
| Google Cloud storage     | Object Storage |                      `Parquet` `CSV` |                                                                                                            |
| Upload file              |      File      |                      `Parquet` `CSV` | Maximum file size is 700MB. <br/>Bigger files should be uploaded and read from <br/>remote object storages |
| Google BigQuery          |   Big Table    |                     `Not applicable` |                                                                                                            |
| MySQL                    |     RDBMS      |                     `Not applicable` | Supports reading whole schemas or specifying a query                                                       |
| Azure SQL Server         |     RDBMS      |                     `Not applicable` | Supports reading whole schemas or specifying a query                                                       |
| PostGreSQL               |     RDBMS      |                     `Not applicable` | Supports reading whole schemas or specifying a query                                                       |
| Snowflake                |     RDBMS      |                     `Not applicable` | Supports reading whole schemas or specifying a query                                                       |
| Oracle DB                |     RDBMS      |                     `Not applicable` | Supports reading whole schemas or specifying a query                                                       |
| Databricks Unity Catalog |    Catalog     |                     `Not applicable` | Supports reading a table                                                                                   |
| Databricks Delta Lake    |   Lakehouse    |                     `Not applicable` | Supports reading a table                                                                                   |

## Haven't found your storage?

To understand our development roadmap or to request prioritization of new data connector, reach out to us at [ydata.ai/contact-us.](https://ydata.ai/contact-us)
