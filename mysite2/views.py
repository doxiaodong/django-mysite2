# coding:utf-8

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token


# Create your views here.
@ensure_csrf_cookie
def init_homepage(request):

    if request.method == "GET":
        csrftoken = get_token(request)
        respose = {
            'status': 1,
            'msg': '请求成功',
            'data': {
                'csrftoken': csrftoken,
                's': [{
                    1: 's',
                    2: 'a'
                }]
            }
        }
        return JsonResponse(respose)
        #
        # context = {
        # 'articleCategory': ArticleCategory.objects.all(),
        #     'articles': Article.objects.filter(category=category),
        # }