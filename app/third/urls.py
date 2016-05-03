# coding:utf-8
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^github/$', views.github, name='github'),
]
