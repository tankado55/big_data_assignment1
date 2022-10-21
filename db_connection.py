from abc import ABC, abstractmethod


class DbConnection (ABC):

    # si portebbe fare con un context manager
    @abstractmethod
    def get_conn(self, server, db_name, credential):
        # qui e in get_data succederanno cose diverse a seconda del db,
        # come funziona il polimorfismo in python?
        pass

    #TODO context manager