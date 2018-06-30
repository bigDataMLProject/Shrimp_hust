from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark import SparkConf
import pyspark.mllib.recommendation as rd

conf = SparkConf().setAppName("miniproject").setMaster("local[*]")
sc = SparkContext.getOrCreate(conf)

sqlContext = SQLContext(sc)
dataframe_mysql_rating = sqlContext.read.format("jdbc").options(url="jdbc:mysql://wander:3306/big_data", driver="com.mysql.jdbc.Driver", dbtable="rating", user="root", password="qwer123").load()

dataframe_mysql_user = sqlContext.read.format("jdbc").options(url="jdbc:mysql://wander:3306/big_data", driver="com.mysql.jdbc.Driver", dbtable="user", user="root", password="qwer123").load()

#sqlContext.registerDataFrameAsTable(dataframe_mysql_user,'user')
# sqlContext.sql('select * from user limit 10').show()

#dataframe_mysql.show()

#schemaNames = dataframe_mysql.schema.fieldNames()       # get columns name -> list

rdd = dataframe_mysql_rating.join(dataframe_mysql_user,dataframe_mysql_user.u_id==dataframe_mysql_rating.u_id).select(dataframe_mysql_user.id,dataframe_mysql_rating.m_id,dataframe_mysql_rating.rate).rdd

#shall be executed by real user id
rdd_ALS = rdd.map(lambda line:rd.Rating((line['id']),int(line['m_id']),float(line['rate'])))      # clear the data to get rating(u,m,r)

model = rd.ALS.train(rdd_ALS,50,10,0.1)

#shall test it when hadoop ok
model.save(sc, "target/tmp/myCollaborativeFilter")
sameModel = MatrixFactorizationModel.load(sc, "target/tmp/myCollaborativeFilter")
