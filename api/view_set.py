# coding:utf-8

from rest_framework import viewsets
from .serializers import *


class ArticleCategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ArticleCategory.objects.all().exclude(url='aabbccddmv')
    serializer_class = ArticleCategoriesSerializer

    lookup_field = 'url'


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    lookup_field = 'url'


class SubCommentsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SubComment.objects.all()
    serializer_class = SubCommentsSerializer


class AccountCommentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer


class LinkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer