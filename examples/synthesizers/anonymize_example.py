import os
import os

from ydata.sdk.dataset import get_dataset
from ydata.sdk.synthesizers import RegularSynthesizer

# Do not forget to add your token as env variables
os.environ["YDATA_TOKEN"] = '<TOKEN>'  # Remove if already defined

def main():
    """In this example, we demonstrate how to train a synthesizer from a pandas
    DataFrame.

    After training a Regular Synthesizer, we request a sample.
    """
    X = get_dataset('titanic')

    # We initialize a regular synthesizer
    # As long as the synthesizer does not call `fit`, it exists only locally
    synth = RegularSynthesizer(name="Titanic")

    # We define anonymization rules, which is a dictionary with format:
    # {column_name: anonymization_rule, ...}
    # while here are some predefined anonymization rules like: name, email, company
    # it is also possible to create a rule using a regular expression
    rules = {
        "Name": "name",
        "Ticket": "[A-Z]{2}-[A-Z]{4}"
    }

    # or a different option for anonymization configuration

    rules = {
        'Name': {'type': 'name'},
        'Ticket': {'type': 'regex',
                   'regex': '[A-Z]{2}-[A-Z]{4}'}
    }

    # We train the synthesizer on our dataset
    synth.fit(
        X,
        anonymize=rules
    )

    # We request a synthetic dataset with 50 rows
    sample = synth.sample(n_samples=50)

    print(sample[["Name", "Ticket"]].head(3))


if __name__ == "__main__":
    main()
