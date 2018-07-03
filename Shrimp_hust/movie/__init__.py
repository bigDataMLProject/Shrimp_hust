from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.mllib.recommendation import MatrixFactorizationModel


conf = SparkConf().setAppName("miniproject").setMaster("local[*]")
sc = SparkContext.getOrCreate(conf)
sqlContext = SQLContext(sc)
model = MatrixFactorizationModel.load(sc, 'file:///tmp/model')
# model.productFeatures().cache()
# model.userFeatures().cache()
