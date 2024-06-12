# Pipelines

The Pipelines module of [YData Fabric](https://ydata.ai/products/fabric) is a general-purpose job orchestrator with built-in scalability and modularity
plus reporting and experiment tracking capabilities.
With **automatic hardware provisioning**, **on-demand** or **scheduled execution**, **run fingerprinting**
and a **UI interface for review and configuration**, Pipelines equip the Fabric with
**operational capabilities for interfacing with up/downstream systems**
(for instance to automate data ingestion, synthesis and transfer workflows) and with the ability to
**experiment at scale** (crucial during the iterative development process required to discover the data
improvement pipeline yielding the highest quality datasets).

YData Fabric's Pipelines are based on ^^[Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/)^^
and can be created via an interactive interface in Labs with Jupyter Lab as the IDE **(recommended)** or
via [Kubeflow Pipeline’s Python SDK](https://www.kubeflow.org/docs/components/pipelines/sdk/sdk-overview/).

With its full integration with Fabric's scalable architecture and the ability to leverage Fabric’s Python interface,
Pipelines are the recommended tool to **scale up notebook work to experiment at scale** or
**move from experimentation to production**.

## Benefits
Using Pipelines for data preparation offers several benefits, particularly in the context of data engineering,
machine learning, and data science workflows. Here are some key advantages:

- **Modularity:** they allow to break down data preparation into discrete, reusable steps.
Each step can be independently developed, tested, and maintained, enhancing code modularity and readability.
- **Automation:** they automate the data preparation process, reducing the need for manual intervention
and ensuring that data is consistently processed. This leads to more efficient workflows and saves time.
- **Scalability:** Fabric's distributed infrastructure combined with kubernetes based pipelines allows to handle
large volumes of data efficiently, making them suitable for big data environments.
- **Reproducibility:** By defining a series of steps that transform raw data into a ready-to-use format,
pipelines ensure that the same transformations are applied every time. This reproducibility is crucial for
maintaining data integrity and for validating results.
Maintainability:
- **Versioning:** support versioning of the data preparation steps. This versioning is crucial
for tracking changes, auditing processes, and rolling back to previous versions if needed.
- **Flexibility:** and above all they can be customized to fit specific requirements of different projects.
They can be adapted to include various preprocessing techniques, feature engineering steps,
and data validation processes.

## Related Materials
- 📖 ^^[How to create your first Pipeline](../get-started/create_pipeline.md)^^
- :fontawesome-brands-youtube:{ .youtube } <a href="https://www.youtube.com/watch?v=feNoXv34waM"><u>How to build a pipeline with YData Fabric</u></a>
