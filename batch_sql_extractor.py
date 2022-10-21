from abc import ABC, abstractmethod
from intercompany_data import IntercompanyData


# Get the stream of NEW DATA (from last month) from the DB and aggregate it in the form of
# intercompany_data to later put them in the historical DB
class BatchSQLExtractor(ABC):
    # Get the stream of NEW DATA (from last month) from the DB and
    # aggregate it in the form of intercompany_data
    @abstractmethod
    def aggregate_from_stream(self, stream_conn, query) -> IntercompanyData:
        pass

    @abstractmethod
    def save_intercompany_data(self, hist_db_conn, intercompany_data: IntercompanyData):
        pass

