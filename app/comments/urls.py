# coding:utf-8

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^add/(?P<article>[-\w]+)/$', views.add_reply, name='add_reply'),
    url(r'^add-sub/(?P<head>[-\w]+)/$', views.add_sub_reply, name='add_sub_reply'),
]
