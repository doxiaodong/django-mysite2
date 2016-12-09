# coding:utf-8
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^lyric/(?P<musicid>[-\w]+)/$$', views.get_lyric_by_id, name='music'),
]
