[![pypi](https://img.shields.io/pypi/v/ydata-sdk)](https://pypi.org/project/ydata-sdk)
[![CondaForge](https://img.shields.io/conda/v/conda-forge/pydantic.svg)](https://anaconda.org/conda-forge/pydantic)
![Pythonversion](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)
[![downloads](https://pepy.tech/badge/pydantic/month)](https://pepy.tech/project/pydantic)
[![license](https://img.shields.io/github/license/pydantic/pydantic.svg)](https://github.com/pydantic/pydantic/blob/main/LICENSE)


<p align="center"><img width="500" src="https://assets.ydata.ai/YData_logo_colored_black.svg" alt="YData Logo"></p>

!!! note "YData SDK for improved data quality everywhere!"

    *ydata-sdk* is coming soon. If you want to know more reach out to us!

    [I want to know more](https://ydata.ai/contact-us){ .md-button .md-button--ydata .md-button--stretch}

## Overview

The *YData SDK* is an ecosystem of methods that allows users to, through a python interface, adopt a *Data-Centric* approach towards the AI development. The solution includes a set of integrated components for data ingestion, standardized data quality evaluation and data improvement, such as *synthetic data generation*, allowing an iterative improvement of the datasets used in high-impact business applications.

**Synthetic data** can be used as Machine Learning performance enhancer, to augment or mitigate the presence of bias in real data. Furthermore, it can be used as a Privacy Enhancing Technology, to enable data-sharing initiatives or even to fuel testing environments. 

Under the YData-SDK hood, you can find a set of algorithms and metrics based on statistics and deep learning based techniques, that will help you to accelerate your data preparation. 

## Current functionality

YData SDK is currently composed by the following main modules:

* **Datasources**
     - YData’s SDK includes several connectors for easy integration with existing data sources. It supports several storage types, like filesystems and RDBMS. Check the list of connectors. 
     - SDK’s Datasources run on top of Dask, which allows it to deal with not only small workloads but also larger volumes of data.

* **Synthesizers**
     - Simplified interface to train a generative model and learn in a data-driven manner the behavior, the patterns and original data distribution. Optimize your model for privacy or utility use-cases.
     - From a trained synthesizer, you can generate synthetic samples as needed and parametrise the number of records needed.

* **Synthetic data quality report**
     *Coming soon*
     - An extensive synthetic data quality report that measures 3 dimensions: privacy, utility and fidelity of the generated data. The report can be downloaded in PDF format for ease of sharing and compliance purposes or as a JSON to enable the integration in data flows.

* **Profiling**
    *Coming soon*
    - A set of metrics and algorithms summarizes datasets quality in three main dimensions: warnings, univariate analysis and a multivariate perspective.

## Supported data formats

=== "Tabular"
    ![Tabular data synthesiszer](https://dummyimage.com/600x400/eee/aaa){ align=right }
    The **RegularSynthesizer** is perfect to synthesize high-dimensional data, that is time-indepentent with high quality results.

    [Know more](#){ .md-button .md-button--ydata}

=== "Time-Series"
    ![Time-series synthesizer](https://dummyimage.com/600x400/eee/aaa){ align=right }
    The **TimeSeriesSynthesizer** is perfect to synthesize both regularly and not evenly spaced time-series, from smart-sensors to stock. 

    [Know more](#){ .md-button .md-button--ydata}

=== "Transactional"
    ![Transactional data synthesizer](https://dummyimage.com/600x400/eee/aaa){ align=right }
    The **TimeSeriesSynthesizer** supports transactional data, known to have highly irregular time intervals between records and directional relations between entities.

    [Know more](#){ .md-button .md-button--ydata}

=== "Relational databases"
    ![Transactional data synthesizer](https://dummyimage.com/600x400/eee/aaa){ align=right }
    The **MultiTableSynthesizer** is perfect to learn how to replicate the data within a relational database schema.
    
    [Know more](#){ .md-button .md-button--ydata}


