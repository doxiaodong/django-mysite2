# coding:utf-8
from django.urls import include, path
from . import views
from . import qq

app_name = 'third'
urlpatterns = [
    path('github/', views.github, name='github'),
    path('qq/', qq.login_route),
]
