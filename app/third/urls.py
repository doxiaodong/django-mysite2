# coding:utf-8
from django.conf.urls import patterns, include, url
from . import views
from . import qq

urlpatterns = [
    url(r'^github/$', views.github, name='github'),
    url(r'^qq/$', qq.login_route),
]
