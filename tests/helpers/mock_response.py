class MockResponse:

    def __init__(self, status_code, json_data=None, reason=None):
        self.status_code = status_code
        self.json_data = json_data
        self.reason = reason

    def json(self):
        return self.json_data
