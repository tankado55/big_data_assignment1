from abc import ABC, abstractmethod
from contextlib import contextmanager


class DbConnection (ABC):

    # Context managers allow you to allocate and release
    # resources precisely when you want to.
    @abstractmethod
    @contextmanager
    def get_conn(self, server, db_name, credential):
        pass
