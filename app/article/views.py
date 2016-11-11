# coding:utf-8

import simplejson
from django.core import serializers
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from .models import *


# Create your views here.
# @csrf_exempt
def article_category(request):
    if request.method == "POST":
        article_categories = ArticleCategory.objects.all()

        respose = {
            'status': 1,
            'msg': '请求成功',
            'data': {
                'article_categories': simplejson.loads(
                    serializers.serialize('json', article_categories, ensure_ascii=False)
                )
            }
        }
        return JsonResponse(respose)

    elif request.method == 'OPTIONS':
        return JsonResponse({})
