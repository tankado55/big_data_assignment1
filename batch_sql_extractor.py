from abc import ABC, abstractmethod
from intercompany_data import IntercompanyData


# This class is used to get the stream of new data from the streaming service
# and aggregate it in the form of intercompany_data to and then
# put them in the historical DB.
# The methods are abstract because the module that provides
# the data stream can change.
class BatchSQLExtractor(ABC):
    # Get the stream of NEW DATA (from last month) from the DB and
    # aggregate it in the form of intercompany_data
    @abstractmethod
    def aggregate_from_stream(self, stream_conn, query) -> IntercompanyData:
        pass

    # Save the newly generated intercompany_data to the Historical DB.
    @abstractmethod
    def save_intercompany_data(self, hist_db_conn, intercompany_data: IntercompanyData):
        pass

