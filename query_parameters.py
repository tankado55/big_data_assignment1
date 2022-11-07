from abc import ABC, abstractmethod

# This class is used to define query parameters for
# different DBs. This class is abstract because it
# can't be instantiated and should be inherited instead.
class QueryParameters():
    tables = None
    month = None
    order = None
    group = None


class QueryParametersStream(QueryParameters):
    pass

class QueryParametersHistorical(QueryParameters):
    pass