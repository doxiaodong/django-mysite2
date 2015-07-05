# coding:utf-8

from django.views.decorators.csrf import ensure_csrf_cookie, get_token
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
import simplejson
from django.core import serializers

from app.article.models import ArticleCategory, Article
from .serializers import ArticleCategoriesSerializer, ArticleListSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


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
        # respose['Access-Control-Allow-Credentials'] = 'true'
        return respose


class ArticleCategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategoriesSerializer


# class ArticleListViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer

class ArticleListViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    # lookup_field = 'url'
    related_name = 'category'
    # def article_list(self, request, category):
    #
    #     # if request.method == 'GET':
    #     if category == 'all':
    #         articles = Article.objects.all()
    #     else:
    #         category = ArticleCategory.objects.get(url=category)
    #         articles = Article.objects.filter(category=category)
    #     serializer = ArticleListSerializer(articles, many=True)
    #     print(serializer.data)
    #     return JSONResponse(serializer.data)