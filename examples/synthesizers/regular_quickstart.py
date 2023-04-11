import os

from ydata.sdk.dataset import get_dataset
from ydata.sdk.synthesizers import RegularSynthesizer

# Do not forget to add your token as env variables
os.environ["YDATA_TOKEN"] = '<TOKEN>'  # Remove if already defined

# In this example, we demonstrate how to train a synthesizer from a pandas DataFrame.
# After training a Regular Synthesizer, we request a sample.

X = get_dataset('titanic')

# We initialize a regular synthesizer
# As long as the synthesizer does not call `fit`, it exists only locally
synth = RegularSynthesizer()

# The synthesizer training is requested
synth.fit(X)

# We request a synthetic dataset with 50 rows
sample = synth.sample(n_samples=50)
