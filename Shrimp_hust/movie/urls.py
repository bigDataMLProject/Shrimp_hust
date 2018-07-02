from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^movie/$', views.index),
    url(r'^type/$', views.search),
    url(r'^movie/detail/$', views.laji),
    url(r'^show', views.show),
    url(r'^login/$', views.login)
]
