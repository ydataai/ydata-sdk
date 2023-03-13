import os

from ydata.sdk.dataset import get_dataset
from ydata.sdk.synthesizers import TimeSeriesSynthesizer

# Do not forget to add your token as env variables
os.environ["YDATA_TOKEN"] = '<TOKEN>'  # Remove if already defined


def main():
    X = get_dataset('airquality')

    # We initialize a regular synthesizer
    # As long as the synthesizer does not call `fit`, it exists only locally
    synth = TimeSeriesSynthesizer()

    # We train the synthesizer on our dataset
    synth.fit(X, sortbykey='Date Local', exclude_cols=['Address'])

    # We request a synthetic dataset with the same length as the original data
    # The TimeSeriesSynthesizer is designed to replicate temporal series and therefore,
    # it is not possible to as for an arbitrarily number of rows.
    sample = synth.sample()

    print(sample.shape)


if __name__ == "__main__":
    main()
