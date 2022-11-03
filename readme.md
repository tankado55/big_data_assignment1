The following is an example architecture for a company that needs to show their Balance Sheet of the last six months.

# Pillar 1: Being the framework for satisfying requirements
To not have impact on the OneStream performance, an Historical Data DB is built to store data extracted from the stream. Only the needed data are extracted from the stream and elaborated as IntercompanyData objects, to satisfy the requirenments and guarantee efficiency.
In this way our front-end module is able to retrieve the necessary data in an efficient way. 

Our Historical DB is sufficently large to store 6 months old data. At the end of the month, analytics are created and data older than 6 months are deleted from the DB. This is done because only datas from six months are required.


# Pillar 2: Being the technical basis for design
Our Architecture is composed of abstract classes that explicit the interactions betweeen the OneStream component, the Historical DB and the front-end client.
These classed are the technical basis for the design process that will follow.

BatchSQLExtractor: Class used to get the stream of new data from OneStrem (EXTRACT) and aggregate (TRANSFORM) it to put them in the Historical DB (LOAD).

AnalyticsProducer: Class used to produce analytics from data retrieved from the Historical DB. It will be used from public APIs in order to provide analytics to external applications.
These application will be in charge of drawing the data in charts, ecc.

# Pillar 3: Being the managerial basis for cost estimation and process management
Defining abstract classes makes us able to estimate the lines of code to write in order to implement our solution.
Lines of code are useful to estimate costs.

# Pillar 4: Enabling component **reuse** 
Component reuse is guaranteed by the use of abstract classes and parametized methods. For example, the DbConnection class can be inherited and its method "get_conn" implemented in different ways, based on the stream provider. The parameters enable us to use the same method for different environment configurations.

# Pillar 5: Allowing a tidy scalability
The aggregation and transformation of data coming from the stream allows for efficiency, speed and scalability. That's because transformed data are easier to retrieve from the DB. In addition, we are able to retrieve data from our Historical DB without overloading the OneStream process with our requests.

# Pillar 6: Avoiding handover and people lock-in
Our code is commented in a way that permit us to avoid people lock-in.
Documentation should also be provided to permit an easy handover when it can't be avoided.
