
# it takes date from historical db and extract analytics
class AnalyticsProducer():

    # private
    def retrieve_data(self, hist_db_conn, query) -> IntercompanyData:
        pass

    def generate_analytics(self, intercompany_data) -> Analytics:
        pass

    # public, uses the two methods above, used by some public api
    def get_analytics(self):
        pass
