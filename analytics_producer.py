from model.analytics import Analytics
from model.intercompany_data import IntercompanyData

# Class used to retrieve data from the Historical DB and extract analytics to
# be provided to the external services.
class AnalyticsProducer():

    # private
    def retrieve_data(self, hist_db_conn, query) -> IntercompanyData:
        pass
    # private
    def generate_analytics(self, intercompany_data) -> Analytics:
        pass

    # public, uses the two methods above, used by the analytics_api
    def get_analytics(self) -> Analytics:
        pass
