# coding:utf-8

from django.urls import include, path
from rest_framework import routers
from . import views, view_set

router = routers.DefaultRouter()
router.register(r'article/categories', view_set.ArticleCategoriesViewSet)
router.register(r'article', view_set.ArticleViewSet)
# router.register(r'subcomments', view_set.SubCommentsViewSet)
router.register(r'comments', view_set.AccountCommentViewSet)
router.register(r'links', view_set.LinkViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path('initHomePage/', views.init_homepage),
    path('article/articles/<category>/', views.ArticleListDetailView.as_view()),
    path('comment/comments/<article>/', views.CommentsDetailView.as_view()),
    path('comment/subcomments/<head>/', views.SubCommentsDetailView.as_view()),
    path('account/subcomments/<user>/', views.AccountSubCommentsDetailView.as_view()),

    path('account/', include('app.account.urls', namespace='account')),
    path('comments/', include('app.comments.urls', namespace='comments')),

    path('third/', include('app.third.urls', namespace='third')),
    path('music/', include('app.music.urls', namespace='music')),
]
