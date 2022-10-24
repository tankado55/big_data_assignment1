from abc import ABC, abstractmethod
from contextlib import contextmanager


class DbConnection (ABC):

    @abstractmethod
    @contextmanager
    def get_conn(self, server, db_name, credential):
        pass
