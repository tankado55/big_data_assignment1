from abc import ABC, abstractmethod


class DataAggregator (ABC):

    @abstractmethod
    def aggregate_month_data(self, conn_stream, conn_aggregated, sql):
        pass

    @abstractmethod
    def get_aggregated_data(self, conn_aggregated, sql):
        pass
