from ydata.sdk.common.model import BaseModel


class Credentials(BaseModel):

    def as_payload(self) -> dict:
        """Convert a credential model to a payload.

        Returns:
            dictionary containing the payload
        """
        return self.dict()
