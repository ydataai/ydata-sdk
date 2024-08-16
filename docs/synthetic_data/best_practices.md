# Best practices for optimal synthetic data generation

## Overview

This document outlines the best practices for generating structured synthetic data, focusing on ensuring data quality, privacy, and utility.
Synthetic data generation is a sophisticated process involving the training of generative models to produce artificial datasets that mimic
real-world data. This documentation is intended to guide data scientists, engineers, and analysts in configuring and refining the synthetic
data generation process, with a focus on avoiding common pitfalls.

### 1. Understanding the Use Case

Before beginning the synthetic data generation process, it is essential to clearly define the use case. 
The purpose of the synthetic data—whether for training machine learning models, testing algorithms, or validating data pipelines—will
influence the structure, scale, and fidelity required.

**Key Considerations:**

*Understand and know your data*: Deeply understanding the characteristics and behaviors of the original dataset is crucial for configuring the synthetic data
generation process to optimize outcomes. This understanding is also essential for validating and assessing the quality of the synthetic data.
If your synthetic data fails to represent all classes from the original dataset, it could indicate that the original data lacks sufficient 
records for those particular behaviors.

- *Data Characteristics:* Identify the necessary size, format, and distribution of the data.

- *Privacy Concerns:* Determine if there are specific regulations or privacy requirements to be met.

- *Critical Variables:* Identify the key variables and relationships that must be preserved in the synthetic data.

### 2. Configuring the Data Schema & Relations

Setting and configuring a concise and business aligned dataset schema is crucial for generating high-quality synthetic data. 
The schema should mirror the structure of the real-world data you aim to emulate, while ensuring the selected *PII Types* and *Data Types*
are aligned with the use-case and applications.  

**Key Considerations:**

- *Data Types:* Make sure to always verify the configured data types. After all learning a "Category" is a different from learning
the distribution for a *Numerical* variable. 

- *Unique Identifiers:* Exclude unique identifiers (e.g., user IDs, transaction IDs) from the data generation process. These identifiers are typically arbitrary and do not carry meaningful information for the generative model to learn. Instead, generate them separately or replace them with randomized values.
Documentation: Thoroughly document the schema, including all constraints and relationships, for future reference and reproducibility.

- *Data Constraints:* Include constraints such as primary keys, foreign keys, and data types to maintain data integrity. Also, make sure
to configure the relation between tables (eg. x= a + b) as it will ensure that the model will treat the outcome for variable x as a deterministic process.

### 3. Avoiding Overfitting to the Original Data

To ensure that the synthetic data is useful and generalizable, it is important to avoid overfitting the generative model to the
original dataset. *YData Fabric* synthetic data generation process leverages the concept of Holdout in order to avoid overfitting, 
but the effectiveness of the holdout might vary depending on the dataset behaviour and size. 

**Key Considerations:**

- *Excessive Fine-Tuning:* Avoid overly fine-tuning the generative model on your whole dataset, as this can lead to synthetic data that
is too similar to the original, reducing its utility.

- *Ignoring Variability:* Ensure that the synthetic data introduces enough variability to cover edge cases and rare events, rather 
than merely replicating common patterns from the training data.

### 4. Ensuring Data Privacy

One of the key benefits of synthetic data is the ability to mitigate privacy risks.
However, careful attention must be paid to ensure that the synthetic data does not inadvertently reveal sensitive information
from the original dataset.

**Key Considerations:**

- *Reusing Identifiable Information:* Do not include direct identifiers (such as names, addresses, etc.) in the synthetic data.

Having a true identifier among the synthetic data might not only hinder the quality of the synthetic data but also its capacity to remain
anonymous.

### 5. Validating the Synthetic Data

Validation is a critical step in the synthetic data generation process.
The synthetic data must be rigorously tested to ensure that it meets the necessary criteria for its intended use. 

**Key Considerations:**

- *Skipping Statistical Validation:* Do not skip the step of comparing the statistical properties of the synthetic data against the
real data. This is essential to ensure that the synthetic data is both realistic and useful.

- *Using a Single Metric:* Avoid relying on a single validation metric. Validate the synthetic data across multiple dimensions, such as distribution, correlation, and predictive performance, to get a comprehensive view of its quality.

YData Fabric synthetic data generation process offers an extensive and automated [synthetic data quality report and profiling
compare](https://ydata.ai/synthetic-data-quality-metrics) to help with the data quality validation. 

### 6. Iterating and Refining the Process

Synthetic data generation is inherently iterative. The initial datasets may require refinement to improve their accuracy, utility, or realism.

**Key Considerations:**

- *Treating the First Version as Final:* The first generated dataset is rarely perfect. Continuous iteration and refinement are key to achieving
high-quality synthetic data.

- *Ignoring Feedback:* Feedback from domain experts and end-users is invaluable. Do not disregard this input, as it can significantly improve
the relevance and utility of the synthetic data.

### 7. Documenting and Sharing the Process

Thorough documentation is essential for transparency, reproducibility, and collaboration in synthetic data generation.

**Key Considerations:**

- *Skipping Documentation:* Failing to document the synthetic data generation process can make it difficult to reproduce results or understand
the rationale behind certain decisions.

- *Keeping the Process Opaque:* Transparency is crucial, especially when synthetic data is used in critical applications.
Ensure that all relevant details, including methodologies, parameters, and assumptions, are clearly documented and accessible to stakeholders.

Before diving into complex applications, ensure you're thoroughly familiar with synthetic data by starting small and gradually increasing complexity.
Build your understanding step by step, and only proceed to more advanced use cases once you're confident in the quality and reliability of the synthetic
data. Know your data and ensure that your synthetic data matches your expectations fully before leveraging it for downstream applications.
