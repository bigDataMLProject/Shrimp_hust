from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark import SparkConf
import pyspark.mllib.recommendation as rd

conf = SparkConf().setAppName("miniproject").setMaster("local[*]")
sc = SparkContext.getOrCreate(conf)

sqlContext = SQLContext(sc)
dataframe_mysql = sqlContext.read.format("jdbc").options(url="jdbc:mysql://wander:3306/big_data", driver="com.mysql.jdbc.Driver", dbtable="rating", user="root", password="qwer123").load()

dataframe_mysql.show()

schemaNames = dataframe_mysql.schema.fieldNames()       # get columns name -> list

rdd_ALS = rdd.map(lambda line:rd.Rating(hash(line['u_id']),int(line['m_id']),float(line['rate'])))      # clear the data to get rating(u,m,r)

