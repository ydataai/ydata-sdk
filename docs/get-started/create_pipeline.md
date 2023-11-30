# How to create your first Pipeline

:fontawesome-brands-youtube:{ .youtube }
Check this quickstart video on <a href="https://youtu.be/_zZBt2nWiH8"><u>how to create your first Pipeline</u></a>.

The best way to get started with Pipelines is to use the interactive Pipeline editor available in the Labs with Jupyter Lab set as IDE.
If you don't have a **Lab** yet, or you don't know how to create one, check our <a href="create_lab"><u>quickstart guide on how to create your first lab</u></a>.

Open an already existing lab.

A Pipeline comprises one or more nodes that are connected (or not!) with each other to define execution dependencies. Each pipeline node
is and should be implemented as a component that is expected to manage a single task, such as read the data, profiling the data, training a model,
or even publishing a model to production environments.

In this tutorial we will build a simple and generic pipeline that use a **Dataset** from Fabric's **Data Catalog** and profile to check it's quality.
We have the notebooks template already available. For that you need to access the *"Academy"* folder as per the image below.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/academy_folder.webp" alt="Academy folder" style="width: 75%;">
</div>

Make sure to copy all the files in the folder "3 - Pipelines/quickstart" to the root folder of your lab, as per the image below.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/copy_files.webp" alt="Select your pipeline editor" style="width: 75%;">
</div>

Now that we have our notebooks we need to make a small change in the notebook "1. Read dataset". Go back to your **Data Catalog**, from one of the datasets
in your Catalog list, select the three vertical dots and click in **"Explore in Labs"** as shown in the image below.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/explore_in_labs.webp" alt="Explore the dataset in the labs" style="width: 70%;">
</div>

The following screen will be shown. Click in copy.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/code_snippet.webp" alt="Dataset code snippet" style="width: 35%;">
</div>

Now that we have copied the code, let's get back to our **"1. Read data.ipynb"** notebook, and replace the first code cell by with the new code. This will allow us to use a
dataset from the Data Catalog in our pipeline.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/og_code.webp" alt="Dataset code snippet" style="width: 50%;">
    <img src="/assets/quickstart/create_pipeline/replaced_code.webp" alt="Dataset code snippet" style="width: 50%;">
</div>

With our notebooks ready, we can now configure our **Pipeline**.
For this quickstart we will be leveraging an already existing pipeline - double-click the file *my_first_pipeline.pipeline*. You should see a pipeline
as depicted in the images below.
To create a new Pipeline, you can open the lab launcher tab and select **"Pipeline Editor"**.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/open_pipeline.webp" alt="Open pipeline" style="width: 40%;">
    <img src="/assets/quickstart/create_pipeline/my_first_pipeline.webp" alt="My first pipeline" style="width: 60%;">
</div>

Before running the pipeline, we need to check each component/step properties and configurations. Right-click each one of the steps, select *"Open Properties"*, and a
menu will be depicted in your right side. Make sure that you have *"YData - CPU"* selected as the **Runtime Image** as show below.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/open_properties.webp" alt="Open pipeline" style="width: 50%;">
    <img src="/assets/quickstart/create_pipeline/runtime_image.webp" alt="My first pipeline" style="width: 50%;">
</div>

We are now ready to create and run our first pipeline. In the top left corner of the pipeline editor, the run button
will be available for you to click.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/run_pipeline.webp" alt="Select your pipeline editor" style="width: 75%;">
</div>

Accept the default values shown in the run dialog and start the run

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/pipeline_default_dialog.webp" alt="Pipeline configuration confirm dialog" style="width: 30%;">
</div>

If the following message is shown, it means that you have create a run of your first pipeline.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/pipeline_creation_success.webp" alt="Select your pipeline editor" style="width: 60%;">
</div>

Now that you have created your first pipeline, you can select the **Pipeline** from Fabric's left side menu.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/pipelines_menu.webp" alt="Select Fabric Pipelines" style="width: 70%;">
</div>

Your most recent pipeline will be listed, as shown in below image.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/my_pipeline_record.webp" alt="My first pipeline listed" style="width: 70%;">
</div>

To check the run of your pipeline, jump into the **"Run"** tab. You will be able to see your first pipeline running!

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/my_first_pipeline_run.webp" alt="My first pipeline listed" style="width: 70%;">
</div>

By clicking on top of the record you will be able to see the progress of the run step-by-step, and visualize the outputs of each and every
step by clicking on each step and selecting the **Visualizations** tab.

<div style="display: flex; justify-content: center;align-items: center;">
    <img src="/assets/quickstart/create_pipeline/pipeline_progress.webp" alt="My first pipeline listed" style="width: 70%;">
</div>

**Congrats!** 🚀 You have now successfully created your first **Pipeline** a code environment, so you can benefit from Fabric's
orchestration engine to crate scalable, versionable and comparable data workflows.
Get ready for your journey of improved quality data for AI.
