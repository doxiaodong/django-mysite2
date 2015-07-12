# coding:utf-8

from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
]