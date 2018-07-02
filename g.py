import pymysql

def recommend_by_movie(movie):
    
    db= pymysql.connect("localhost","root","19961116","mv",charset="utf8")
    cur=db.cursor()
    #movie="功夫"
    sql1="SELECT m_id FROM movie WHERE m_name='%s'" %(movie)
    cur.execute(sql1)
    db.commit()
    mid=cur.fetchone()
    m_id=int(mid[0])
    

    sql2="SELECT m_id FROM movie WHERE m_name<>'%s'" %(movie)
    cur.execute(sql2)
    db.commit()
    ID_list=[]
    s=cur.fetchone()
    while(s!=None):
        ID_list.append(s[0])
        s=cur.fetchone()

    movie_or_feature=[]
    sql3="SELECT * FROM movie WHERE m_id='%d'" %(m_id)
    cur.execute(sql3)
    db.commit()
    d=cur.fetchone()
    for i in d:
        movie_or_feature.append(i)


    movie_the_feature=[]
    for i in movie_or_feature:
        wordlist=[]
        word=''
        for s in str(i):
        
            if(s=='/'):
                wordlist.append(word)
                word=''
            else:
                word=word+s
        wordlist.append(word)

        movie_the_feature.append(wordlist)
            
            


    movie_feature=[]
    for x in ID_list:
        count=0
        movie_f=[]
        sql="SELECT *FROM movie WHERE m_id='%d'" %(int(x))
        cur.execute(sql)
        db.commit()
        f=cur.fetchone()
        for i in f:
            movie_f.append(i)

        movie_features=[]

        for i in movie_f:
            wordlist=[]
            word=''
            for s in str(i):
                if(s=='/'):
                    wordlist.append(word)
                    word=''
                else:
                    word=word+s
            wordlist.append(word)
        

            movie_features.append(wordlist)
        
        for i in movie_the_feature[2]:
            if i in movie_features[2]:
                count=count+0.25
            
                break
                     
        for i in movie_the_feature[4]:
            if i in movie_features[4]:
                count=count+0.25
                #print("it work!")
                break

        for i in movie_the_feature[5]:
            if i in movie_features[5]:
                count=count+0.25
                #print("it work!")
                break
        
                     
        for i in movie_the_feature[6]:
            if i in movie_features[6]:
                #print("it work!")
                count=count+0.25
                break
        movie_feature_list=[]
        movie_feature_list.append(x)
        movie_feature_list.append(count)
    
        movie_feature.append(movie_feature_list)
        
    


    recommend_list=[]
    for i in movie_feature:
        if(i[1]==1):
            if(len(recommend_list)<5):
                recommend_list.append(i[0])
                
            else:
                break

    if(len(recommend_list)<5):
        for i in movie_feature:
            if(i[1]==0.75):
                if(len(recommend_list)<5):
                    recommend_list.append(i[0])
                    print("抱歉，没有更多相关推荐")
                else:
                    break

            
    if(len(recommend_list)<5):
        for i in movie_feature:
            if(i[1]==0.5):
                if(len(recommend_list)<5):
                    recommend_list.append(i[0])
                    print(i[1])
                else:
                    break

    if(len(recommend_list)<5):
        for i in movie_feature:
            if(i[1]==0.25):
                if(len(recommend_list)<5):
                    recommend_list.append(i[0])
                    print(i[1])
                else:
                    break
    if(len(recommend_list)<5):
        print("抱歉，没有更多相关推荐")

    movie_list={}
    for i in range(1,6):
        sql="SELECT m_name,type,imgurl FROM movie WHERE m_id='%d'" %(int(recommend_list[i-1]))
        cur.execute(sql)
        db.commit()
        li=cur.fetchone()
        movie_list["name"+str(i)]=li[0]
        movie_list["type"+str(i)]=li[1]
        movie_list["url"+str(i)]=li[2]

    return movie_list
    
