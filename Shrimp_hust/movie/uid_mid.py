from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.mllib.recommendation import MatrixFactorizationModel

conf = SparkConf().setAppName("miniproject").setMaster("local[*]")
sc = SparkContext.getOrCreate(conf)
sqlContext = SQLContext(sc)

def recommendationM(uid):
    url_ = "jdbc:mysql://wander:3306/big_data"
    driver_ = "com.mysql.jdbc.Driver"
    table = "user"
    dataf = sqlContext.read.format("jdbc").options(url=url_, driver=driver_, dbtable=table, user="root", password="qwer123").load()
    sqlContext.registerDataFrameAsTable(dataf,'user')

    id =  sqlContext.sql("select id from user where user.u_id ="+"'"+str(uid)+"'").take(1)[0]['id']

    model=MatrixFactorizationModel.load(sc,'/tmp/model')

    result = list(map(lambda x:x[1],model.recommendProducts(id,13)))
    return result

if __name__ = '__main__':
    print(recommendationM('zzxxyy')


>>>>>>> 781ae6d97531e6e6dc9389df218c0bcf6c5083a3

