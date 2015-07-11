from django.conf.urls import patterns, include, url
from rest_framework import routers
from . import views, view_set


router = routers.DefaultRouter()
router.register(r'article/categories', view_set.ArticleCategoriesViewSet)
router.register(r'article', view_set.ArticleViewSet)
router.register(r'subcomments', view_set.SubCommentsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^initHomePage/$', views.init_homepage),
    url(r'^article/articles/(?P<category>\w+)/$', views.ArticleListDetailView.as_view()),
    url(r'^comment/comments/(?P<article>\w+)/$', views.CommentsDetailView.as_view()),
    url(r'^comment/subcomments/(?P<head>\w+)/$', views.SubCommentsDetailView.as_view()),
]