The first technical step in any data science project is to examine the data and understand its quality, value and fitness for purpose. For this reason,  Fabric’s Data Catalog includes an **Overview and Warnings** module  for a better understanding of the available datasets.

## Overview
When clicking on a **Dataset** available from the **Data Catalog**, it will show its details page, revealing an **Overview and Warnings** section.

<figure markdown>
![Dataset Overview](../../assets/data_catalog/dataset_overview.png){: style="height:550px;width:1200px"}
</figure>

In the **Overview**, you’ll get an overall perspective of your dataset’s characteristics, where descriptive statistics will be presented, including:

- Basic description and tags/concepts associated to the dataset
- Memory consumption
- Number of rows
- Duplicate rows (percentage / number of records)
- Number of columns
- Total data types (numeric, categorical, string, long text, ID, date)
- Missing data (percentage / number of cells)
- Main data quality warnings


## Data Quality Warnings
To enable data-centric development, Fabric **automatically detects and signals potential data quality warnings**. Warnings highlight certain peculiarities of data that might require further investigation prior to model development and deployment. However, *the validity of each issued warning and whether follow-up mitigation work is needed will depend on the specific use case and on domain knowledge*.

<figure markdown>
![Dataset Warnings](../../assets/data_catalog/data_warnings.png){: style="height:300px;width:1000px"}
</figure>

Fabric currently supports the following warnings:

- **Constant:** the column presents the same value for all observations
- **Zeros:**  the column presents the value “0” for several observations
- **Unique:** the column contains only unique/distinct values
- **Cardinality:** the columns (categorical) has a large number of distinct values
- **Infinity:** the column presents infinite ($\inf$) values
- **Constant_length**: the column (text) has constant length
- **Correlation:** the columns is highly correlated with other(s)
- **Skeweness**: the column distribution (numerical) is skewed
- **Missings:** the column presents several missing values
- **Non-stationarity:** the column (time series) presents statistical properties that change through time
- **Seasonal:** the column (time series) exhibits a seasonal pattern
- **Uniform:** the column (numerical) follows a uniform distribution
- **Imbalance:** the column (categorical) presents a high imbalance ratio between existing categories

Fabric further enables the **interactive exploration of warnings**, filtering over specific warnings and severity types (i.e., **Moderate** and **High**):

<figure markdown>
![Explore Warnings](../../assets/data_catalog/explore_warnings.png){: style="height:630px;width:700px"}
</figure>
