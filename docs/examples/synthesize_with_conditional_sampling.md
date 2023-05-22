# Conditional sampling

YData Synthesizers support conditional sampling. The `fit` method has an optional parameter named `condition_on`, which receives a list of features to condition upon. Furthermore, the `sample` method receives the conditions to be applied through another optional parameter also named `condition_on`. For now, two types of conditions are supported:

- Condition upon a categorical (or string) feature. The parameters are the name of the feature and a list of values (i.e., categories) to be considered. Each category also has its percentage of representativeness. For example, if we want to condition upon two categories, we need to define the percentage of rows each of these categories will have on the synthetic dataset. Naturally, the sum of such percentages needs to be 1. The default percentage is also 1 since it is the required value for a single category.
- Condition upon a numerical feature. The parameters are the name of the feature and the minimum and maximum of the range to be considered. This feature will present a uniform distribution on the synthetic dataset, limited by the specified range.


The example below demonstrates how to train and sample from a synthesizer using conditional sampling:

```python
--8<-- "examples/synthesizers/conditional_sampling_example.py"
```
