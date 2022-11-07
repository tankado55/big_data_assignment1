# from db_connection import OnestreamConnection
# from batch_sql_extractor import OnestreamBatchSQLExtractor
# from data_visualizer import GrafanaDataVisualizer

def main():
    with OnestreamConnection.get_conn(server, db_name, credential) as conn:
      new_data = OnestreamBatchSQLExtractor.aggregate_from_stream(conn, query)
      OnestreamBatchSQLExtractor.save_intercompany_data(hist_db_conn, new_data)

    # intercompany_data = AnalyticsProducer.get_analytics()
    # A 3rd party application will  be responsible to use our API to retrieve
    # the analitycs of the intercompany data and then draw them.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

