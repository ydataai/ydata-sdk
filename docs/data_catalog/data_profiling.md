
To enable a full understanding of the available data assets, Fabric further incorporates a module for **Data Profiling**, which allows you to further investigate the characteristics of your dataset more deeply, zooming in on the behavior and relationships between particular columns.

???+ question "Profiling Large Datasets?"
	We've got you covered. [Fabric Data Catalog](https://ydata.ai/products/data_catalog) offers an interactive, flexible, and intuitive experience when handling datasets with **thousands of columns and any number of rows**. Learn more about the benefits of Fabric in [profiling high-dimensional datasets](https://ydata.ai/resources/understanding-large-multivariate-data-with-data-profiling) and sign up for the [Community Version](https://ydata.ai/ydata-fabric-free-trial) to experiment with your own data assets.

The data profiling essentially enables the following analysis:

- **Univariate Analysis and Feature Statistics:** Fabric incorporates **type inference**, automatically detecting the data types in a dataset. Depending on the column’s data type, **adjusted descriptive statistics** are presented. The same applies for the **visualizations** chosen for each column.

- **Multivariate Analysis and Correlation Assessment:** To enable multivariate analysis and the evaluation of existing relationships between columns, Fabric includes informative visualizations regarding the **interactions** and **correlations** between columns, and the investigation of **missing data** and **outliers**.

<figure markdown>
![Connectors](../assets/data_catalog/profiling_heatmap.png){: style="height:550px;width:1200px"}
</figure>


The data profiling highlights a set of **statistical properties**, such as:

- **Variables Properties**: 
	- Descriptive statistics
	- Quantile statistics
	- Histogram, Common Values, and Extreme Values
- **Interactions and Correlations**:
	- Heat maps and bar plot formats with interactive selection;
	- Spearman’s and Cramer’s V analysis
- **Missing Values (MAR, MNAR, and MCAR):**
	- Count and Matrix
- **Autoregressive and Stationarity Detection** <span style="color:grey">***(Time Series Data)***</span>
	- ACF and PACF analysis
- **Text Analysis**
	- Most occurring characters, words, categories, among others

???+ tip "Profiling Sensitive Data?"
	By default, Fabric assumes that any data to be profile **can contain sensitive information**. For that reason, it includes several features to enable a **secure and fair data profiling** such as the *aggregation of easily-identifiable groups* and the *obfuscation of values* for categorical columns. Sign up for the [Community Version](https://ydata.ai/ydata-fabric-free-trial) and move towards a **responsible exploration** of your data.