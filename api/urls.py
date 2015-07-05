from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


router = routers.DefaultRouter()
router.register(r'article/categories', views.ArticleCategoriesViewSet)
router.register(r'article/articles', views.ArticleListViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^initHomePage/$', views.init_homepage),
    # url(r'^article/articles/(?P<category>\w+)$', views.article_list),
]