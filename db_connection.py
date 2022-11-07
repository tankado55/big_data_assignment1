from abc import ABC, abstractmethod
from contextlib import contextmanager


class DbConnection (ABC):

    # Context managers allows you to allocate and release
    # resources precisely when you want to.
    # This abstract method is used to create the connection with both the streaming
    # service and the Historical DB. This method will be implemented in different
    # ways depending on the chosen streaming service and Historical DB.
    @abstractmethod
    @contextmanager
    def get_conn(self, server, db_name, credential):

        pass
