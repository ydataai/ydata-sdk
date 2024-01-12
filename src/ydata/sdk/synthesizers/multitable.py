from time import sleep

from ydata.sdk.common.client import Client
from ydata.sdk.common.config import BACKOFF
from ydata.sdk.common.exceptions import InputError
from ydata.sdk.common.types import UID, Project
from ydata.sdk.datasources import DataSource
from ydata.sdk.synthesizers.synthesizer import BaseSynthesizer


class MultiTableSynthesizer(BaseSynthesizer):
    """MultiTable synthesizer class.

    Methods
    -------
    - `fit`: train a synthesizer instance.
    - `sample`: request synthetic data.
    - `status`: current status of the synthesizer instance.

    Note:
            The synthesizer instance is created in the backend only when the `fit` method is called.

    Arguments:
        write_connector (UID): Connector of type RDBMS to be used to write the samples
        name (str): (optional) Name to be used when creating the synthesizer. Calculated internally if not provided
        client (Client): (optional) Client to connect to the backend
    """

    def __init__(
            self, write_connector: UID, uid: UID | None = None, name: str | None = None,
            project: Project | None = None, client: Client | None = None):

        self.__write_connector = write_connector

        super().__init__(uid, name, project, client)

    def fit(self, X: DataSource) -> None:
        """Fit the synthesizer.

        The synthesizer accepts as training dataset a YData [`DataSource`][ydata.sdk.datasources.DataSource].

        Arguments:
            X (DataSource): DataSource to Train
        """

        self._fit_from_datasource(X)

    def sample(self, frac: int | float = 1, write_connector: UID | None = None) -> None:
        """Sample from a [`MultiTableSynthesizer`][ydata.sdk.synthesizers.MultiTableSynthesizer]
        instance.
        The sample is saved in the connector that was provided in the synthesizer initialization
        or in the

        Arguments:
            frac (int | float): fraction of the sample to be returned
        """

        assert frac >= 0.1, InputError(
            "It is not possible to generate an empty synthetic data schema. Please validate the input provided. ")
        assert frac <= 5, InputError(
            "It is not possible to generate a database that is 5x bigger than the original dataset. Please validate the input provided.")

        payload = {
            'fraction': frac,
        }

        if write_connector is not None:
            payload['writeConnector'] = write_connector

        response = self._client.post(
            f"/synthesizer/{self.uid}/sample", json=payload, project=self._project)

        data = response.json()
        sample_uid = data.get('uid')
        sample_status = None
        while sample_status not in ['finished', 'failed']:
            self._logger.info('Sampling from the synthesizer...')
            response = self._client.get(
                f'/synthesizer/{self.uid}/history', project=self._project)
            history = response.json()
            sample_data = next((s for s in history if s.get('uid') == sample_uid), None)
            sample_status = sample_data.get('status', {}).get('state')
            sleep(BACKOFF)

        print(
            f"Sample created and saved into connector with ID {self.__write_connector or write_connector}")

    def _create_payload(self) -> dict:
        payload = super()._create_payload()
        payload['writeConnector'] = self.__write_connector

        return payload
