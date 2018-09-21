# coding:utf-8

from django.urls import include, path
from . import views

app_name = 'comments'
urlpatterns = [
    path('add/<article>/', views.add_reply, name='add_reply'),
    path('add-sub/<head>/', views.add_sub_reply, name='add_sub_reply'),
]
