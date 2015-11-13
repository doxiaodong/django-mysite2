# coding:utf-8
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
		url(r'^github/$', views.get_code, name='get_code'),
]