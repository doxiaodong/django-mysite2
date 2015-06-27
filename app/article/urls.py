# coding:utf-8
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns(
    '',
    # url(r'^(?P<category>\w+)/(?P<pk>\d+)/$', views.detail, name='article_detail'),
    # url(r'^all/$', views.article_view, name='article_view'),
    # url(r'^(?P<category>\w+)/$', views.article_list, name='article_list'),


    url(r'^getArticleCategory/$', views.article_category, name='article_category'),
)