import os

from ydata.sdk.connectors import Connector
from ydata.sdk.datasources import DataSource
from ydata.sdk.synthesizers import MultiTableSynthesizer

# Do not forget to add your token as env variables
os.environ["YDATA_TOKEN"] = '<TOKEN>'  # Remove if already defined

# In this example, we demonstrate how to train a synthesizer from an existing multi table RDBMS datasource.
# After training a Multi Table Synthesizer, we request a sample.
# In this case, we don't return the Dataset for the sample, it will be saved in the database
# that the connector refers to.

X = DataSource.get('<DATASOURCE_UID>')

# For demonstration purposes, we will use a connector instance, but you can just send the UID

write_connector = Connector.get('<CONNECTOR_UID>')

# Initialize a multi table synthesizer with the connector to write to
# As long as the synthesizer does not call `fit`, it exists only locally
# write_connector can be an UID or a Connector instance
synth = MultiTableSynthesizer(write_connector=write_connector)

# The synthesizer training is requested
synth.fit(X)

# We request a synthetic dataset with a fracion of 1.5
# In this case we use a Connector instance.
# You can just use the <CONNECTOR_UID> you don't need to get the connector upfront.
synth.sample(frac=1.5, write_connector=write_connector)
