
# Class that represents the Analytics object that will be
# provided to the external services.
class Analytics():

    def __init__(self, value1, value2, value3):
        self._value1: value1
        self._value2: value2
        self._value3: value3

    @property
    def get_value1(self):
        return self._value1

    @property
    def get_value2(self):
        return self._value2

    @property
    def get_value3(self):
        return self._value3

    # This method will be used to send the Analytics object to the
    # 3rd party application in JSON format.
    def to_json(self):
        pass