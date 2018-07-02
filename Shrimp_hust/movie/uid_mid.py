from movie.__init__ import *



def recommendationM(uid):

    url_ = "jdbc:mysql://wander:3306/big_data"
    driver_ = "com.mysql.jdbc.Driver"
    table = "user"



    dataf = sqlContext.read.format("jdbc").options(url=url_, driver=driver_, dbtable='user', user="root", password="qwer123").load()
    datam = sqlContext.read.format("jdbc").options(url=url_, driver=driver_, dbtable='movie', user="root", password="qwer123").load()

    sqlContext.registerDataFrameAsTable(dataf,'user')
    sqlContext.registerDataFrameAsTable(datam,'movie')

    row =  sqlContext.sql("select id from user where user.u_id ="+"'"+str(uid)+"'")
    fixed = sqlContext.sql("select id from user where user.u_id = 'zzxxyy'")

    mn=[]
    mid=[]
    rmovie={}

    if row.count() == 0:
        id = fixed.take(1)[0]['id']
        mid = list(map(lambda x:x[1],model.recommendProducts(id,13)))

    else :
        id = row.take(1)[0]['id']
        mid = list(map(lambda x:x[1],model.recommendProducts(id,13)))

    for x in range(len(mid)):
        mn.append ( sqlContext.sql("select m_name from movie where m_id ="+"'"+str(mid[x])+"'").take(1)[0]['m_name'])
        rmovie['rname'+str(x)] =mn[x]

    return rmovie
