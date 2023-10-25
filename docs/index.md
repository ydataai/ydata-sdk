# What is Fabric?

Fabric is a Data-Centric AI workbench that **accelerates AI development by helping data scientists achieve production-quality data**. It is an end-to-end data development solution that can be hosted on cloud environments (e.g., Azure, AWS, and GCP, among others) or on-prem.

!!! note "Ready to achieve high-quality data to train you machine learning models?"

    *Fabric Community Version* is free! Create a YData account so you can start using today!

    [Create account](https://ydata.ai/ydata-fabric-free-trial){ .md-button .md-button--ydata .md-button--stretch}

With Fabric data scientists can explore **automated quality profiling** for a deeper understanding of their data assets, and leverage **smart synthetic data** to unlock data-sharing initiatives, improve data through augmentation or rebalancing, and mitigate bias in their datasets.

<p align="center"> <iframe width="600" height="400" src="https://www.youtube.com/embed/ccF0RaxVLrk" title="Fabric -  The data development platform for improved AI performance" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></p>

Fabric includes a set of integrated components for data ingestion, data profiling, data quality evaluation, and synthetic data generation, including the following functionalities:

- **Data Catalog:** Simplified, scalable, and seamless connection to a variety of object storages, data warehouses, and relational database management systems, with detailed visual data univariate and multivariate analysis combined with automatic detection of data quality issues;
- **Labs:** On-demand JupyterLab, Visual Studio Code or H2O Flow development environments with configurable hardware (including GPUs), supercharged with the most popular data science libraries and [YData Python SDK](sdk/index.md) – a code interface to most of the functionalities, ideal for advanced use cases;
- **Synthetic Data:** Simplified interface to train state-of-the-art Machine Learning models able to generate artificial data mimicking a specific Data Source, and assess the quality of the new data according to the 3 essential pillars of fidelity, utility, and privacy;
- **Pipelines:** General-purpose job orchestrator with built-in scalability, modularity, reporting, and experiment-tracking capabilities, useful for iterative experimentation at scale.


??? tip "Fabric's Data-Centric AI Flow"
    While each module provides value by itself, **when used together they enable a compelling data-centric narrative arc** that goes from data exploration to data improvement while abstracting away shared core needs like infrastructure, data access, and workspace management:


    ![Fabric Data-Centric Flow](../assets/overview/fabric_data_centric_flow.png){: style="height:398px;width:1042px;align:center"}


## Data Catalog

Fabric’s Catalog is a project-based data repository that enables data scientists to discover, understand, and access relevant datasets. It provides a **comprehensive inventory of available Connectors and Data Sources**, along with **descriptive metadata** that allows data scientists to swiftly and efficiently locate and evaluate existing data sources, assess their quality, and gain insights into the data's structure and content.

<p align="center"><iframe width="600" height="400" src="https://www.youtube.com/embed/3JyuJlQLM4Q" title="Data profiling in a single click" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></p>

The Data Catalog facilitates data exploration, promotes data reuse, and accelerates the overall data science workflow, including the following benefits:

- Easy data ingestion supporting various types of storage from RDBMs to Cloud Object Storage;
- A curated and discoverable list of datasets per project;
- An overview and detailed metadata of your datasets;
- Extensive data profiling for thorough and standardized data quality assessment.


???+ question "Looking for a full Data Understanding experience?"
    Enable a seamless data exploration of your organization's data assets with [Fabric Data Catalog](https://ydata.ai/products/data_catalog), which allows consuming data from RDBMs (Azure SQL, PostGreSQL, Oracle) and object storages (Google Cloud Storage, AWS S3, Snowflake), and interactive profiling of large volumes of data.

## Synthetic Data

Fabric’s Synthetic Data allows data scientists to leverage advanced Machine Learning models to **create high-quality synthetic data** that mimics the characteristics and behavior of real data while maintaining data privacy. This technology unlocks **privacy-enhanced data sharing**, fosters data quality through **data augmentation**, and boosts the fairness and generalization ability of AI models by **increasing the diversity of training datasets** through the tailored generation of underrepresented concepts in real data.

<p align="center"><iframe width="600" height="400" src="https://www.youtube.com/embed/GsfggG9PhgE" title="How to generate synthetic data from a CSV" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></p>

The Synthetic Data module includes the following functionalities:

- Comprehensive support for tabular, time-series, transactional data, and relational databases;
- Optimized and automatic model selection for synthetic data generation;
- Tailored synthetic data generation, enabling anonymization, business controls and conditional sampling;
- Customizable privacy control for optimized trade-offs between fidelity, and utility, privacy;
- Flexible synthetic data quality assessment in a standard PDF format.


???+ question "Should I buy or build a synthetic data generation solution?"
    If you’re looking to fully unlock your assets for data sharing or secure development initiatives for your organization, open-source solutions will not be able to cope with your specific business needs, data flow’s complexity, and scale. Fabric’s interfaces (GUI and code) enable different profiles within an organization to leverage the benefits of synthetic data, from data stewards and quality assurance engineers all the way to data analysts and data scientists. Learn more about Fabric's main features and benefits [by downloading this whitepaper](https://ydata.ai/whitepaper-sdv-vs-fabric).


## Labs

Laboratories (referred to as **Labs**) are on-demand, cloud-based data development environments with automatically provisioned hardware. Labs enable a full platform integration via the YData Python SDK, allowing users to easily access Data Sources, Synthesizers, and the workspace’s shared files. 

<p align="center"><iframe width="600" height="400" src="https://www.youtube.com/embed/ccF0RaxVLrk?t=44" title="Fabric - The data development platform for improved AI performance" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></p>

Labs further incorporate the following:

- Multiple infrastructure configurations, including GPUs;
- Integration with popular data science IDEs, including Visual Studio Code, Jupyter Lab, and H2O Flow;
- Support for both R and Python with preconfigured data science bundles such as TensorFlow and PyTorch.

???+ question "Why should I use Labs?"
    Labs exist for Data Scientists to tackle more complex use cases through a familiar environment supercharged with infrastructure, integration with other Platform modules and access to advanced synthesis and profiling technology via a familiar SDK.
    It is the preferred environment for Data Scientists to express their domain expertise with all the required tools, technology, and computational power at their fingertips. It is thus the natural continuation of the data understanding works which started in the Data Catalog.

## Pipelines

Pipelines allow data scientists to treat code snippets as building blocks, enabling them to **build scalable and complex workflows** while leveraging Jupyter Notebooks or Python scripts. From data transformations to data synthesis, model training, or inference, **pipelines enable the orchestration of any job**, allowing data teams to explore and compare the effects of different data preparation decisions.

<p align="center"><iframe width="600" height="400" src="https://www.youtube.com/embed/feNoXv34waM" title="How to build data quality pipelines with YData Fabric" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></p>

Additionally, pipelines offer the following:

- Customizable infrastructure configurations per step for optimal performance;
- Git versioning for reproducibility and version control;
- Comparison and versioning of pipeline runs;
- Configurable recurrency to automate repeated tasks.

???+ example "Learn how to use Pipelines with YData's Academy examples"
    To understand how to best apply the full capabilities of Pipelines in real world use cases, check out the [use cases section of YData’s Academy](https://github.com/ydataai/academy/tree/master/4%20-%20Use%20Cases). Most use cases include a pipeline leveraging common and use-case specific features of the Pipelines module. These pipelines are offered in `.pipeline` files which can be interactively explored in Jupyter Lab, inside Labs.

## SDK

The YData Python SDK acts as a Python interface to the functionalities available in Fabric, providing an **ecosystem of methods that allow users to leverage the benefits of Fabric inside code environments**. YData SDK offers some of the same components for data ingestion and data quality evaluation and improvement as Fabric, currently incorporating the following modules:

- **Connectors and Data Sources**, including the RDBMs and Cloud Object Storage available in the Data Catalog;
- **Synthetic Data**, including anonymization, privacy control, and conditional sampling and supporting all data types, from tabular, time-series, transactional, and relational databases;
- **Synthetic Data Quality Report** <span style="color:grey">*Coming soon*</span>
- **Data Profiling** <span style="color:grey">*Coming soon*</span>

???+ example "Starting out with YData SDK?"
    For full details and installation and quickstart instructions, check the [SDK dedicated section.](../sdk/index.md)
