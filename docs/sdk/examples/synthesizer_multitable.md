# Synthesize Relational databases

**Integrate Fabric's *MultiTableSynthesizer* in your data flows and generate synthetic relational databases or multi-table datasets**

The capability to generate synthetic data from relational databases is a powerful and innovative approach to
streamline the access to data and improve data democratization strategy within the organization.
Fabric's SDK makes available an easy-to-use code interface to integrate the process of generating synthetic multi-table databases
into your existing data flows.

!!! tip "How to get your datasource?"
    Learn how to create your multi-table data in Fabric <a href="/get-started/create_multitable_dataset"><u>here</u></a> before creating your first multi-table synthetic data generator!

    **Get your datasource and connector ID**

    *Datasource uid:* You can find your datasource ID through Fabric UI. Open your relational dataset and click in the "Explore in Labs" button.
    Copy the uid that you find available in the code snippet.

    *Connector uid:* You can find your connector ID through Fabric UI. Open the connector tab from your Data Catalog. Under the connector "Actions"
    select "Explore in Lab". Copy the uid available in the code snippet.

Quickstart example:

```python
--8<-- "examples/synthesizers/multi_table_quickstart.py"
```
