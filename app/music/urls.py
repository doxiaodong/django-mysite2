# coding:utf-8
from django.urls import include, path
from . import views

app_name = 'music'
urlpatterns = [
    path('lyric/<musicid>/', views.get_lyric_by_id, name='music'),
]
