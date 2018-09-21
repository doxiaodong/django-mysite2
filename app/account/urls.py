# coding:utf-8

from django.urls import include, path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('getUserInfo/', views.get_user, name='get_user'),
    path('setting/', views.setting, name='setting'),
    path('change/', views.change, name='change'),
    path('reset/', views.reset, name='reset'),
]
