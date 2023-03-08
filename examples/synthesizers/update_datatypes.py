import os

from ydata.sdk.dataset import get_dataset
from ydata.sdk.synthesizers import RegularSynthesizer

# Do not forget to add your token as env variables
os.environ["YDATA_TOKEN"] = '<TOKEN>'  # Remove if already defined


def main():
    """In this example, we demonstrate how modify the datatype of a column
    during the synthesization.

    Changing the datatype might be needed in case the type inference is not as
    expected. For instance, a column is deduced as numerical but for your use
    case, it should be considered as categorical.
    """
    X = get_dataset('census')

    dataset_attrs = {
        'columns_types': [
            {
                'name': 'education-num',
                'datatype': 'categorical'  # Originally deduced as numerical
            }
        ]
    }

    # We initialize a regular synthesizer
    # As long as the synthesizer does not call `fit`, it exists only locally
    synth = RegularSynthesizer()

    # We train the synthesizer on our dataset
    synth.fit(X, dataset_attrs=dataset_attrs)

    # We request a synthetic dataset with 50 rows
    sample = synth.sample(n_samples=50)

    print(sample.head())


if __name__ == "__main__":
    main()
