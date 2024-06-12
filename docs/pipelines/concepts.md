# Concepts

An example pipeline (as seen in the Pipelines module of the dashboard), where each single-responsibility block corresponds to a step in a typical machine learning workflow

Each Pipeline is a set of connected blocks. A block is a self-contained set of code, packaged as a container, that performs one step in the Pipeline. Usually, each Pipeline block corresponds to a single responsibility task in a workflow. In a machine learning workflow, each step would correspond to one block, i.e, data ingestion, data cleaning, pre-processing, ML model training, ML model evaluation.

Each block is parametrized by:

- **code:** it executes (for instance, a Jupyter Notebook, a Python file, an R script)
- **runtime:** which specifies the container environment it runs in, allowing modularization and inter-step independence of software requirements (for instance, specific Python versions for different blocks)
- **hardware requirements:** depending on the workload, a block may have different needs regarding CPU/GPU/RAM. These requirements are automatically matched with the hardware availability of the cluster the Platform’s running in. This, combined with the modularity of each block, allows cost and efficiency optimizations by up/downscaling hardware according to the workload.
- **file dependencies:** local files that need to be copied to the container environment
- **environment variables**, useful, for instance to apply specific settings or inject authentication credentials
- **output files**: files generated during the block’s workload, which will be made available to all subsequent Pipeline steps

The hierarchy of a Pipeline, in an ascending manner, is as follows:

- **Run:** A single execution of a Pipeline. Usually, Pipelines are run due to changes on the code,
on the data sources or on its parameters (as Pipelines can have runtime parameters)
- **Experiment:** Groups of runs of the same Pipeline (may have different parameters, code or settings, which are
then easily comparable). All runs must have an Experiment. An Experiment can contain Runs from different Pipelines.
- **Pipeline Version:** Pipeline definitions can be versioned (for instance, early iterations on the flow of operations;
different versions for staging and production environments)
- **Pipeline**

📖 ^^[Get started with the concepts and a step-by-step tutorial](../get-started/create_pipeline.md)^^

## Runs & Recurring Runs
A *run* is a single execution of a pipeline. Runs comprise an immutable log of all experiments that you attempt,
and are designed to be self-contained to allow for reproducibility. You can track the progress of a run by looking
at its details page on the pipeline's UI, where you can see the runtime graph, output artifacts, and logs for each step
in the run.

A *recurring run*, or job in the backend APIs, is a repeatable run of a pipeline.
The configuration for a recurring run includes a copy of a pipeline with all parameter values specified
and a run trigger. You can start a recurring run inside any experiment, and it will periodically start a new copy
of the run configuration. You can enable or disable the recurring run from the pipeline's UI. You can also specify
the maximum number of concurrent runs to limit the number of runs launched in parallel.
This can be helpful if the pipeline is expected to run for a long period and is triggered to run frequently.
## Experiment
An experiment is a workspace where you can try different configurations of your pipelines. You can use experiments to organize
your runs into logical groups. Experiments can contain arbitrary runs, including recurring runs.
## Pipeline & Pipeline Version
A pipeline is a description of a workflow, which can include machine learning (ML) tasks, data preparation or even the
generation of synthetic data. The pipeline outlines all the components involved in the workflow and illustrates how these
components interrelate in the form of a graph. The pipeline configuration defines the inputs (parameters) required to run
the pipeline and specifies the inputs and outputs of each component.

When you run a pipeline, the system launches one or more Kubernetes Pods corresponding to the steps (components)
in your workflow. The Pods start Docker containers, and the containers, in turn, start your programs.

Pipelines can be easily versioned for reproducibility of results.
## Artifacts
For each block/step in a Run, **Artifacts** can be generated.
Artifacts are raw output data which is automatically rendered in the Pipeline’s UI in a rich manner - as formatted tables, text, charts, bar graphs/scatter plots/line graphs,
ROC curves, confusion matrices or inline HTML.

Artifacts are useful to attach, to each step/block of a data improvement workflow, relevant visualizations, summary tables, data profiling reports or text analyses.
They are logged by creating a JSON file with a simple, pre-specified format (according to the output artifact type).
Additional types of artifacts are supported (like binary files - models, datasets), yet will not benefit from rich visualizations in the UI.

!!! tip "Compare side-by-side"
    💡 **Artifacts** and **Metrics** can be compared side-by-side across runs, which makes them a powerful tool when doing iterative experimentation over
    data quality improvement pipelines.

## Pipelines examples in YData Academy
👉 ^^[Use cases on YData’s Academy](https://github.com/ydataai/academy/tree/master/4%20-%20Use%20Cases)^^ contain examples of full use-cases as well as Pipelines interface to log metrics and artifacts.
