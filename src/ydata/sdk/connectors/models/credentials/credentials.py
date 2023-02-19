from ydata.sdk.common.model import BaseModel


class Credentials(BaseModel):

    def as_payload(self) -> dict:
        return self.dict()
