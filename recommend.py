import operator
import re
import math
from pyspark import SparkContext
from pyspark import SparkConf
import pyspark.mllib.recommendation as rd

def trainValidation(td,vd):
    d = dict()
    for rank in [5,10,15,20,50,100]:
        for it in [5,10,15,20,25]:
            for lam in [0.05,0.1,1.0,5.0,10.0]:
                rmse = trainModel(td,vd,rank,it,lam)
                d[rmse] = (rank,it,lam)
# {rmse:(rank,it,lam)} rmse is the distance () is the paras
    print(d[min(d)])

def trainModel (traindata,validationdata,r,i,l):
    model = rd.ALS.train(traindata,r,i,l)
    return computeRmse(model,validationdata)

def computeRmse(model,validationdata):

    predictedRDD = model.predictAll(validationdata.map(lambda x:(x[0],x[1])))
    predictedANDRatings = predictedRDD.map(lambda x:((x[0],x[1]),x[2]))
    
    return math.sqrt(predictedANDRatings.join(validationdata.map(lambda x:((x[0],x[1]),x[2]))).map(lambda x:math.pow((x[1][0]-x[1][1]),2)).reduce(operator.add)/validationdata.count())


conf = SparkConf().setAppName("miniproject").setMaster("local[*]")
sc = SparkContext.getOrCreate(conf)

rdd = sc.textFile("/home/simon/Downloads/ml-100k/u1.base")

rawRatings = rdd.map(lambda line:line.split('\t')[0:3])
ratings = rawRatings.map(lambda x:rd.Rating(int(x[0]),int(x[1]),float(x[2])))

'''
model = rd.ALS.train(ratings,50,10,0.01)
predictedRating = model.predict(3,132)
print (predictedRating)
topKRecs = model.recommendProducts(789, 10)
print(topKRecs)
'''

(traindata,validationdata,testdata) = ratings.randomSplit([0.8,0.1,0.1])    #return traindata validation data, test data
#traindata.persist(),validationdata,testdata

bestModel = trainValidation(traindata,validationdata)

testRmse = computeRMSE(bestModel,testdata)


