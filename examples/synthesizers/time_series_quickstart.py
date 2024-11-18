# -*- coding: utf-8 -*-

# Authentication
import os

from ydata.sdk.dataset import get_dataset
from ydata.sdk.synthesizers import TimeSeriesSynthesizer

# Do not forget to add your token as env variable
os.environ["YDATA_TOKEN"] = '{insert-token}'


# Sampling an example dataset for a multientity & multivariate time-series dataset"""

# Generate the dataset
time_series_data = get_dataset('timeseries')

# Print the first few rows of the dataset
print(time_series_data.head())

# Train a Synthetic data generator

# From a pandas dataframe

# We initialize a time series synthesizer
# As long as the synthesizer does not call `fit`, it exists only locally
synth = TimeSeriesSynthesizer(name='Time-series synth')

# We train the synthesizer on our dataset
# sortbykey -> variable that define the time order for the sequence
synth.fit(time_series_data, sortbykey='time', entities='entity_id')

# Generate samples from an already trained synthesizer
# From the synthesizer in context in the notebook


# Generate a sample with x number of entities
# In this example the objective is to generate a dataset with the same size as the original. For that reason, 5 entities will be generated.
sample = synth.sample(n_entities=5)

sample.head()

# From a previously trained synthetic data generation model
# List the trained synthetic data generators to get the uid synthetisizer
TimeSeriesSynthesizer.list()

synth = TimeSeriesSynthesizer(uid='{insert-synth-id}').get()

# Generate a new synthetic dataset with the sample method
sample = synth.sample(n_entities=5)

sample.head()
