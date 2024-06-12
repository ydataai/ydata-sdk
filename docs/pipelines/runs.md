# Creating & managing runs

## Viewing Run details

To view a specific Run, we need to go into the **Experiments** list and click on the desired Run. Alternatively, accessing **Runs** and selecting directly the desired run is possible. 

![Acessing Runs through its Experiment](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Untitled%202.png)

Acessing Runs through its Experiment

![Viewing the full list of Runs, for all Pipelines and Experiments. Runs can be filtered and sorted based on different fields (including Metrics).](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Untitled%203.png)

Viewing the full list of Runs, for all Pipelines and Experiments. Runs can be filtered and sorted based on different fields (including Metrics).

Once a Run is selected, its graph can be viewed (and in real-time, if the Run is being executing). The graph shows the execution status of each log. Clicking on each block will reveal the block’s details, including artifacts, various configuration details and logs (useful for troubleshooting). 

![The details page of a step, showing a profiling report (as HTML) as an Artifact](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Untitled%204.png)

The details page of a step, showing a profiling report (as HTML) as an Artifact

The **Run Output** tab includes outputs such as metrics or binary artifacts. 

## Creating Runs

Besides triggering Execution via the pipeline editor in Jupyter Lab or the Python SDK, the Pipelines management UI can also be used. 

### One-off

To create a one-off run of a Pipeline, choose a Pipeline in the *Pipelines* section (including the specific Pipeline version, in case there are multiple definitions) and click *+ Create Run*. 

![Creating a Run of a specific Pipeline](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Untitled%205.png)

Creating a Run of a specific Pipeline

To finish creating the Run, additional information is needed: 

- a **Description** (optional)
- the **Experiment** (mandatory and can be chosen from the list of existing ones)
- the **Run Type** (which should be one-off)
- any eventual runtime **parameters** of the Pipeline.

![Untitled](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Untitled%206.png)

Clicking *Start* ****will trigger execution. Each Run will have a unique, automatically created ID.

<aside>
💡 One-off runs are useful for, for instance, quickly trying out different parameters or for stable data pipelines where the input data has changed (unexpectedly) and the pipelines needs to be ran again.

</aside>

### Recurring

To create a Recurring Run, the procedure shown above should be followed, but instead a *Recurring* **Run Type** should be chosen.

The main configuration parameters of a Recurring Run are the **frequency**, **start date** and **end date**, as well as the **maximum number of concurrent Runs** of the Pipeline. The maximum number of concurrent Runs is a particularly relevant parameter for Pipelines whose execution time may stretch into the following’s scheduled Run start time - it should be tweaked to avoid overwhelming the available infrastructure. Recurrency can also be configured via cron-like definitions.

![Configuring a Recurrent Run](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Untitled%207.png)

Configuring a Recurrent Run

The recurring run will keep on executing until its end date or until it is manually disabled. Configured Recurrent Runs are listed on the *Recurring Runs* section.

<aside>
💡 Recurring runs are useful in several situations:

- determining the average execution time of a Pipeline (in case there are run-dependent time fluctuations)
- when any of the inputs (for instance, input data read from a remote location) changes at a predictable pace
</aside>

# Creating a Pipeline

The recommended way to create a Pipeline is to use the interactive Pipeline editor available on Labs with Jupyter Lab set as IDE. It allows the:

- addition of blocks by dragging and dropping notebooks/Python scripts/R scripts (can be a mixture)
- connecting blocks in linear and non-linear ways to define the execution sequence
- configuring the parameters of each block in-line.

[Building a simple synthetic data generation pipeline in the interactive editor by dragging and dropping Jupyter Notebooks (Python/R files could also be dragged), leveraging input files for credentials, environment variables for workflow settings, software runtime specification and per-block hardware needs.](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Screen_Recording_2022-07-27_at_18.29.08.mov)

Building a simple synthetic data generation pipeline in the interactive editor by dragging and dropping Jupyter Notebooks (Python/R files could also be dragged), leveraging input files for credentials, environment variables for workflow settings, software runtime specification and per-block hardware needs.

The built Pipeline can be directly ran from the editor. It will then be automatically available in the dashboard’s web UI, where it can be viewed and managed.

<aside>
👉 To build Pipelines fully via code (in any Python IDE), refer to the [Kubeflow Pipelines SDK](https://www.kubeflow.org/docs/components/pipelines/sdk/sdk-overview/).

</aside>

# Managing Pipelines

The Pipelines management interface is accessible in the platform’s dashboard, via the sidebar item *Pipelines*.

![The Pipelines management module](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Untitled%201.png)

The Pipelines management module

It has 6 main sub-modules:

- **Pipelines**: list of existing Pipelines, which can be further drilled-down into the versions of each Pipeline, as Pipeline definitions can be versioned.
- **Experiments:** a ****list of all available Experiments (groups of Runs), regardless of their origin Pipeline.
- **Runs:** a ****list of all available Runs, regardless of their origin Pipeline/Experiment.
- **Recurring Runs:** an interface to view and configure the Runs triggered on a schedule.
- **Artifacts:** list of Artifacts generated by all Runs of all Pipelines
- **Executions:** a list of all executed blocks/steps across all Runs of all Pipelines

<aside>
💡 Pipelines created via code can be compiled to a `.pipeline` file, which can then be submited via the *+ Upload pipeline* button.

</aside>


## Creating a new Experiment

An experiment is used to group together the runs of a single or different Pipelines. It is particularly useful for organization and Artifacts/Metrics comparison purposes.

To create a new Experiment, access the *Experiments* section and click *+ Create Experiment*. An Experiment requires a name and an optional description. 

## Comparing Runs

**Comparing runs is particularly useful in iterative data improvement scenarios**, as Artifacts, Metrics and Parameters can be directly compared side-by-side. Runs using different pre-processing techniques, settings, algorithms can be put against each other side-by-side in a visual and intuitive interface. 

To compare multiple Runs, select the Runs of interest (either from the *Experiments* or *Runs* pane) and select *Compare runs:*

![Selecting Runs to compare from the Experiments list](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Untitled%208.png)

Selecting Runs to compare from the Experiments list

![In case of this particular data quality improvement Pipeline, the Metrics of each Run are shown side by side.](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Untitled%209.png)

In case of this particular data quality improvement Pipeline, the Metrics of each Run are shown side by side.

Up to 10 runs can be selected for side-by-side comparison. In case any step of the Run has logged Artifacts, the equivalent Artifacts are shown in a comparative interface. 

![Comparing the confusion matrices of three Runs of a Pipeline, which were logged as Artifacts during one of the Pipeline’s steps.](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Screenshot_from_2020-10-24_01-12-27.png)

Comparing the confusion matrices of three Runs of a Pipeline, which were logged as Artifacts during one of the Pipeline’s steps.

## Cloning Runs

For full reproducibility purposes, it is possible to select a previous run and clone it. Cloned runs will use exactly the same runtime input parameters and settings. However, **any time dependent inputs (like the state of a remote data source at a particular point in time) will not be recreated**.

To clone a Run, click the *Clone run* button available in a Run’s detail page or in the list of Runs/Experiment (when a single Run is selected). It will be possible to review the settings prior to triggering the execution. 

## Archiving Runs

Archiving a Run will move it to the Archived section the *Runs* and *Experiments* list. This section can be used to save older executions, to highlight best runs or to record anomalous executions which require further digging into. 

Archive a Run by clicking the *Archive* button from the Run’s details page (or from the list of Runs/Experiments when a Run is selected). 

![The Archived section, which is in all ways similar to the list of Active buttons. The *Restore* button (highlighted) moves Runs between the two sections.](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Untitled%2010.png)

The Archived section, which is in all ways similar to the list of Active buttons. The *Restore* button (highlighted) moves Runs between the two sections.

When a Run is archived, it can be restored through the *Restore* button.

---

<aside>
💡 **Learn by example**

To understand how to best apply the full capabilities of Pipelines in real world use cases, check out the [use cases section of YData’s Academy](https://github.com/ydataai/academy/tree/master/5%20-%20use-cases).

Most use cases include a pipeline leveraging common and use case specific features of the Pipelines module. These pipelines are offered in  `.pipeline` files which can be interactively explored in Jupyter Lab, inside Labs.

</aside>

[](Pipelines%2055c1a84b8a374deab72652d8f3fc375c/Untitled%20cb6afa6dc57e4efdbda8f94de7b67340.md)
