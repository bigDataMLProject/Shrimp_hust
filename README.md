# Shrimp_hust
one recommend system like taobao able to recommend movies to specific user based on bigdata and machine learning
网页链接 ： http://134.175.19.214/Mymovie/login/

version 1.0.0
前端界面：


已完成

* 页面跳转
* 选择分类

未完成

* 推荐接口对接
* 搜索关键字

![1530350870483](assert/1530350870483.png)



ALS算法model 存储在hadoop:/tmp/model/

* 未与前端对接
* 推荐相似电影
------------------------------------
version 1.0.1

**part1**
前端界面：     **唐**

已完成
* 页面跳转
* 选择分类
* 登陆
* 搜索
* 推荐1
* 推荐2
* 详细信息页
* 用户信息侧边栏
* 各种界面美化

未完成
* logo
* 超级搜索
* 用户注册


![1530350870483](assert/login.png)
![1530350870483](assert/index.png)
![1530350870483](assert/user.png)
![1530350870483](assert/detail.png)


**part2**     **齐**
针对用户推荐
* 模型优化
* 模型保存
* 模型推荐
![training srceenshot](assert/training_sc.png)
代码文件 
* train_rating.py
* uid_mid.py

**part3**     **张**
针对电影推荐
* 特征融合

代码文件
* g.py
