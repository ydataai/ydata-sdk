import numpy as np
import pandas as pd

from ydata.sdk.synthesizers import RegularSynthesizer


def main():
    # Let's create a small random dataset
    X = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))

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
