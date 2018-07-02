from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^movie/$', views.index),  # 主页面
    url(r'^type/$', views.search),  # 根据类型划分
    url(r'^movie/detail/$', views.laji),  # 电影详细信息页面
    url(r'^show', views.show),  # 根据电影名返回电影详细信息
    url(r'^login/$', views.login),  # 登录主界面
    url(r'^getid', views.getid),    # 获取用户名，并返回推荐电影
    url(r'^select', views.select_movie)  # 完成搜索功能
]
