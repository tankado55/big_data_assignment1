The following is an example architecture for a company that needs to show their Balance Sheet of the last six months.

# Pillar 1: Being the framework for satisfying requirements
To not have impact on the OneStream performance, an Historical Data DB is built to store data extracted from the stream.
In this way our front-end module is able to retrieve the necessary data in an efficient way. 

Our Historical DB is sufficently large to store 6 months old data. At the end of the month, analytics are created and datas older than 6 months are deleted from the DB. This is done because only datas from six months are required. 

# Pillar 2: Being the technical basis for design
Our Architecture is composed of abstract classes that explicit the interactions betweeen the OneStream component, the Historical DB and the front-end client.

BatchSQLExtractor: Class used to get the stream of new data from OneStrem and aggregate it to put them in the Historical DB.

AnalyticsProducer: Class used to produce analytics from datas kept in the Historical DB.

DataVisualizer: 


# Context manager

sometimes you have to deal with multiple database connectors (in the data exploration phase, for example), and you’ll have to read from each of them on a regular basis. This might introduce some redundancy, which suggests that a reusable function might be a good fit for this scenario.

# an alternative: decorator

**salvo le analytics**. Prossimo mese eliminerò i dati pi vecchi di 6 mesi. (Da esplicitare nel codice)

**ASSUNZIONE**: I dati più vecchi di 6 mesi vengono eliminati dal DB per salvare spazio eperchè non richiesti da requirements.
### Definire algoritmi 
es. Non fare il batch da zero ogni mese ma sfruttare 5 mesi prima e aggiungerci l'ultimo mese.