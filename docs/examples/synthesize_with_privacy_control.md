# Privacy control

YData Synthesizers offers 3 different levels of privacy:

1. **high privacy**: the model is optimized for privacy purposes,
2. **high fidelity** (default): the model is optimized for high fidelity,
3. **balanced**: tradeoff between privacy and fidelity.

The default privacy level is high fidelity. The privacy level can be changed by the user at the moment a synthesizer level is trained by using the parameter [`privacy_level`](../reference/api/synthesizers/timeseries/#ydata.sdk.synthesizers.timeseries.TimeSeriesSynthesizer.fit).
The parameter expect a [`PrivacyLevel`](../reference/api/synthesizers/base/#privacylevel) value.


!!! question "What is the difference between anonymization and privacy?"

    **Anonymization** makes sure sensitive information are hidden from the data.    
    **Privacy** makes sure it is not possible to infer the original data points from the synthetic data points via statistical attacks.

    Therefore, for data sharing **anonymization** and **privacy** controls are complementary.



The example below demonstrates how to train a synthesizer configured for high privacy:

```python
--8<-- "examples/synthesizers/privacy_example.py"
```
