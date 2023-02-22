from pathlib import Path

import pandas as pd

from ydata.sdk.synthesizers import RegularSynthesizer

# Do not forget to add your token as env variables


def main():
    # Let's load a small random dataset
    X = pd.read_csv(Path(__file__).parent / 'data/dummy.csv')

    # We initialize a regular synthesizer
    # As long as the synthesizer does not call `fit`, it exists only locally
    synth = RegularSynthesizer()

    # We train the synthesizer on our dummy dataset
    synth.fit(X)

    # We request a synthetic dataset with 50 rows
    sample = synth.sample(n_samples=50)

    print(sample.shape)


if __name__ == "__main__":
    main()
