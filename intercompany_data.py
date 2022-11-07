
# Class that represents aggregated data from the stream.
# Every object has a timestamp and an other_company parameter
# to identify the company it was generated from.
# There are additional parameters (value1, value2 ecc) that
# can be filled with additional infos of interest.
class IntercompanyData(object):

    def __init__(self):
        self._timestamp = None
        self._other_company = None
        self._value1 = None
        self._value2 = None
        self._value3 = None

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @timestamp.deleter
    def timestamp(self):
        del self._timestamp

    @property
    def other_company(self):
        return self._other_company

    @other_company.setter
    def other_company(self, value):
        self._other_company = value

    @other_company.deleter
    def other_company(self):
        del self._other_company
