# coding:utf-8

from django.views.decorators.csrf import ensure_csrf_cookie, get_token
from django.http import JsonResponse, HttpResponse
import simplejson
import json
from django.core import serializers as core_serializers

from .serializers import *
from rest_framework import viewsets, generics


# Create your views here.
@ensure_csrf_cookie
def init_homepage(request):
    if request.method == "GET":
        request.session['user'] = 'new'
        respose = JsonResponse({
            'status': 1,
            'msg': 'success',
            'data': {
                'csrftoken': get_token(request)
            }
        })
        return respose


class ArticleListDetailView(generics.ListAPIView):
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        if category == 'all':
            articles = Article.objects.all()
        elif category == 'hot':
            articles = Article.objects.filter(hot=True)
        else:
            category = ArticleCategory.objects.get(url=category)
            articles = Article.objects.filter(category=category)

        return articles


class CommentsDetailView(generics.ListAPIView):

    serializer_class = CommentsSerializer

    def get_queryset(self):
        article = self.kwargs['article']
        article = Article.objects.filter(url=article)
        comments = Comment.objects.filter(article=article)

        index = 1

        for head in comments:
            sub = SubComment.objects.filter(head=head)
            head.sub_comment = simplejson.loads(
                core_serializers.serialize('json', sub, ensure_ascii=False)
            )
            head.index = index
            index += 1

        return comments


class SubCommentsDetailView(generics.ListAPIView):

    serializer_class = SubCommentsSerializer

    def get_queryset(self):
        head = self.kwargs['head']
        head = Comment.objects.filter(url=head)
        sub_comments = SubComment.objects.filter(head=head)

        return sub_comments
