class MockRequestResult:
    def __init__(self, jsonBlob):
        self.parsedJsonBlob = jsonBlob
    def json(self):
        return self.parsedJsonBlob