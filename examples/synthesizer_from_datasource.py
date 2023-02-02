import os

from ydata.sdk.connectors import Connector
from ydata.sdk.datasources import DataSource
from ydata.sdk.synthesizers import RegularSynthesizer

# Do not forget to add your token as env variables
os.environ["YDATA_TOKEN"] = '<TOKEN>'


def main():
    """In this example, we demonstrate how to create a Google Cloud Storage
    connector using a credentials file.

    Then, we create a DataSource using this connector and train a
    RegularSynthesizer. Finally, we sample from the trained Synthesizer.
    """

    # Path to the Google Cloud Storage credentials file
    credentials = "./.secrets/gcs_credentials.json"  # Change-me!

    # We create a new connector for Google Cloud Storage
    connector = Connector(connector_type='gcs', credentials=credentials)

    # We now create a datasource from our connector
    # Note that a connector can be re-used for several datasources
    X = DataSource(connector=connector, path='gs://<my_bucket>.csv')

    # Note that it is possible to change the file type and separator via:
    # ds = DataSource(connector=connector, path='gs://<my_bucket>/*', filetype='parquet', separator=';')

    # We initialize a regular synthesizer
    # As long as the synthesizer does not call `fit`, it exists only locally
    synth = RegularSynthesizer()

    # We train the synthesizer on our dummy dataset
    synth.fit(X)

    # We request a synthetic dataset with 50 rows
    sample = synth.sample(n_samples=50)

    print(sample.head())


if __name__ == "__main__":
    main()
