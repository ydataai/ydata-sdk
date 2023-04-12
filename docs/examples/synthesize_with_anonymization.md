# Anonymization

YData Synthesizers offers a way to anonymize sensitive information such that the original values are not present in the synthetic data but replaced by **fake** values.

!!! note "Does the model retain the original values?"

    No! The anonymization is performed before the model training such that it never sees the original values.

The anonymization is performed by specifying which columns need to be anonymized and how to performed the anonymization.
The anonymization rules are defined as a dictionary with the following format:

`{column_name: anonymization_rule}`

While here are some predefined anonymization rules such as `name`, `email`, `company`, it is also possible to create a rule using a regular expression.
The anonymization rules have to be passed to a synthesizer in its `fit` method using the parameter [`anonymize`](../reference/api/synthesizers/timeseries/#ydata.sdk.synthesizers.timeseries.TimeSeriesSynthesizer.fit).

!!! question "What is the difference between anonymization and privacy?"

    **Anonymization** makes sure sensitive information are hidden from the data.
    **Privacy** makes sure it is not possible to infer the original data points from the synthetic data points via statistical attacks.

    Therefore, for data sharing **anonymization** and **privacy** controls are complementary.

The example below demonstrates how to anonymize the column `Name` by fake names and the column `Ticket` by a regular expression:
```python
--8<-- "examples/synthesizers/anonymize_examples.py"
```
