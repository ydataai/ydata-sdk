import os

from ydata.sdk.dataset import get_dataset
from ydata.sdk.synthesizers import RegularSynthesizer

# Do not forget to add your token as env variables.
os.environ["YDATA_TOKEN"] = '<TOKEN>'  # Remove if already defined.


def main():
    """In this example, we demonstrate how to train and
    sample from a synthesizer using conditional sampling."""
    X = get_dataset('census')

    # We initialize a regular synthesizer.
    # As long as the synthesizer does not call `fit`, it exists only locally.
    synth = RegularSynthesizer()

    # We train the synthesizer on our dataset setting
    # the features to condition upon.
    synth.fit(
        X,
        name="census_synthesizer",
        condition_on=["sex", "native-country", "age"]
    )

    # We request a synthetic dataset with specific condition rules.
    sample = synth.sample(
        n_samples=500,
        condition_on={
            "sex": {
                "categories": ["Female"]
            },
            "native-country": {
                "categories": [("United-States", 0.6),
                               ("Mexico", 0.4)]
            },
            "age": {
                "minimum": 55,
                "maximum": 60
            }
        }
    )
    print(sample)


if __name__ == "__main__":
    main()
