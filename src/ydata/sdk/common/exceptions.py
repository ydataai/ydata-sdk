from typing import Optional

from ydata.core.error import FabricError


class SDKError(Exception):
    """Base Exception for all SDK errors."""


class ResponseError(FabricError):
    """Wrapper around Fabric Exception to capture error response from the
    backend."""

    def __init__(
            self,
            context: Optional[dict[str, str]] = None,
            httpCode: Optional[int] = None,
            name: Optional[str] = None,
            description: Optional[str] = None,
            returnValue: Optional[str] = None):
        self.description = description
        self.return_value = returnValue
        FabricError.__init__(self, context=context, http_code=httpCode, name=name)


class ClientException(SDKError):
    """Base Exception for Client related exceptions."""


class ClientCreationError(ClientException):
    """Raised when a Client could not be created."""


class ConnectorError(SDKError):
    """Base exception for ConnectorError."""


class InvalidConnectorError(ConnectorError):
    """Raised when a connector is invalid."""


class CredentialTypeError(ConnectorError):
    """Raised when credentials are not formed properly."""


class DataSourceError(SDKError):
    """Base exception for DataSourceError."""


class DataSourceNotAvailableError(DataSourceError):
    """Raised when a datasource needs to be available."""


class SynthesizerException(SDKError):
    """Base Exception for Synthesizer related exception."""


class NotReadyError(SynthesizerException):
    """Raised when a Synthesizer is not read."""


class NotTrainedError(SynthesizerException):
    """Raised when a Synthesizer is not trained."""


class NotInitializedError(SynthesizerException):
    """Raised when a Synthesizer is not initialized."""

    def __init__(self, message="The synthesizer is not initialized.\n Use `fit` to train the synthesizer or `get` to retrieve an existing instance."):
        super().__init__(message)


class AlreadyFittedError(SynthesizerException):
    """Raised when a Synthesizer is already trained."""

    def __init__(self, message="The synthesizer is already fitted!"):
        super().__init__(message)


class FittingError(SynthesizerException):
    """Raised when a Synthesizer fails during training."""


class InputError(SDKError):
    """Raised for any user input related error."""
