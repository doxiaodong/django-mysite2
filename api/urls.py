# coding:utf-8

from django.conf.urls import patterns, include, url
from rest_framework import routers
from . import views, view_set

router = routers.DefaultRouter()
router.register(r'article/categories', view_set.ArticleCategoriesViewSet)
router.register(r'article', view_set.ArticleViewSet)
# router.register(r'subcomments', view_set.SubCommentsViewSet)
router.register(r'comments', view_set.AccountCommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^initHomePage/$', views.init_homepage),
    url(r'^article/articles/(?P<category>\w+)/$', views.ArticleListDetailView.as_view()),
    url(r'^comment/comments/(?P<article>\w+)/$', views.CommentsDetailView.as_view()),
    url(r'^comment/subcomments/(?P<head>\w+)/$', views.SubCommentsDetailView.as_view()),
    url(r'^account/subcomments/(?P<user>\w+)/$', views.AccountSubCommentsDetailView.as_view()),

    url(r'^account/', include('app.account.urls', namespace='account')),
    url(r'^comments/', include('app.comments.urls', namespace='comments')),
]