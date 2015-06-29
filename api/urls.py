from django.conf.urls import patterns, include, url
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'article/categories', views.ArticleCategoriesViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^initHomePage/$', views.init_homepage),
]