from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark import SparkConf

conf = SparkConf().setAppName("miniproject").setMaster("local[*]")
sc = SparkContext.getOrCreate(conf)
sqlContext = SQLContext(sc)

def recommendationM(uid):
    url_ = "jdbc:mysql://wander:3306/big_data"
    driver_ = "com.mysql.jdbc.Driver"
    table = "rating"
    dataf = sqlContext.read.format("jdbc").options(url=url_, driver=driver_, dbtable=table, user="root", password="qwer123").load()
    sqlContext.registerDataFrameAsTable(dataf,'user')

    id =  sqlContext.sql('select id from user where u_id ='+str(uid)).take(1)[0]['id']
    model
    result = model.recommendProducts(id,10)
