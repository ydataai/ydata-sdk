import os

from ydata.sdk.dataset import get_dataset
from ydata.sdk.synthesizers import TimeSeriesSynthesizer

# Do not forget to add your token as env variable
os.environ["YDATA_TOKEN"] = '<TOKEN>'

X = get_dataset('airquality')

# We initialize a regular synthesizer
# As long as the synthesizer does not call `fit`, it exists only locally
synth = TimeSeriesSynthesizer()

# We train the synthesizer on our dataset
# sortbykey -> variable that define the time order for the sequence
# exclude_cols -> columns that we want to remove from the synthesis process
synth.fit(X, sortbykey='Date Local', exclude_cols=['Address'])

# By default it is requested a synthetic sample with the same length as the original data
# The TimeSeriesSynthesizer is designed to replicate temporal series and therefore the original time-horizon is respected
sample = synth.sample()
