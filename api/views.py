# coding:utf-8

from django.views.decorators.csrf import ensure_csrf_cookie, get_token
from django.http import JsonResponse

from app.article.models import ArticleCategory
from .serializers import ArticleCategoriesSerializer
from rest_framework import viewsets


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
        respose['Access-Control-Allow-Credentials'] = 'true'

        return respose


class ArticleCategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategoriesSerializer
