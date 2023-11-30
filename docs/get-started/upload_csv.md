# How to create your first Dataset from a CSV file

:fontawesome-brands-youtube:{ .youtube }
Check this quickstart video on <a href="https://youtu.be/1zYreRKsNGE"><u>how to create your first Dataset from a CSV file</u></a>.

To create your first dataset in the **Data Catalog**, you can start by clicking on **"Add Dataset"** from the Home section.
Or click to **Data Catalog** (on the left side menu) and click **“Add Dataset”**.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/upload_csv/welcome_add_dataset.png" alt="Add dataset from Home" style="width: 75%;">
</div>

After that the below modal will be shown. You will need to select a connector. To upload a CSV file, we need to select **“Upload CSV”**.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/upload_csv/data_catalog_connectors.png" alt="Select connectors to storage" style="width: 45%;">
</div>

Once you've selected the **“Upload CSV”** connector, a new screen will appear, enabling you to upload your file and designate a name for your connector.
This file upload connector will subsequently empower you to create one or more datasets from the same file at a later stage.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/upload_csv/loading_area.png" alt="Upload file area" style="width: 45%;">
    <img src="/assets/quickstart/upload_csv/load_csv_file.png" alt="Upload CSV file" style="width: 45%;">
</div>

With the *Connector* created, you'll be able to add a dataset and specify its properties:

- **Name:** The name of your dataset;
- **Separator:** This is an important parameter to make sure that we can parse your CSV correctly. The default value is “,”.
- **Data Type:** Whether your dataset contains tabular or time-series (i.e., containing temporal dependency) data.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/upload_csv/add_dataset_details.png" alt="Upload file area" style="width: 45%;">
</div>

Your created Connector *(“Census File”)* and Dataset *(“Census”)* will be added to the Data Catalog.
As soon as the status is green, you can navigate your Dataset. Click in **Open Dataset** as per the image below.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/upload_csv/open_dataset.png" alt="Upload file area" style="width: 75%;">
</div>

Within the **Dataset** details, you can gain valuable insights through our automated data quality profiling.
This includes comprehensive metadata and an overview of your data, encompassing details like row count, identification
of duplicates, and insights into the overall quality of your dataset.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/upload_csv/dataset_overview.png" alt="Upload file area" style="width: 75%;">
</div>

Or perhaps, you want to further explore through visualization, the profile of your data with both univariate
and multivariate of your data.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/upload_csv/dataset_profiling.png" alt="Upload file area" style="width: 75%;">
</div>

**Congrats!** 🚀 You have now successfully created your first **Connector** and **Dataset** in Fabric’s Data Catalog.
Get ready for your journey of improved quality data for AI.
