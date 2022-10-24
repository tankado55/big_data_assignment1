from abc import ABC, abstractmethod
from intercompany_data import IntercompanyData
# Take the intercompany_data from the historical DB
# and visualize it
class DataVisualizer(ABC):

    @abstractmethod
    def retrieve_data(self, hist_db_conn, query) -> IntercompanyData:
        pass

    @abstractmethod
    def draw_data(self, intercompany_data, visualization_parameters):
        pass


    # Add pie or other chart visual methods (?)