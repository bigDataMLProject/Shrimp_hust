from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^movie/$', views.index),
    url(r'^type/$', views.search)
]
