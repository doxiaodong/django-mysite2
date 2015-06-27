# coding:utf-8

from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import *


# Create your views here.
@csrf_exempt
def article_category(request):
    if request.method == "POST":
        articleCategories = ArticleCategory.objects.all()

        respose_categories = []
        for category in articleCategories:
            respose_categories.append({
                'url': category.url,
                'name': category.name
            })

        respose = {
            'status': 1,
            'msg': '请求成功',
            'data': {
                # 'articleCategories': eval(serializers.serialize('json', articleCategories))
                'articleCategories': respose_categories
            }
        }
        return JsonResponse(respose)
        #
        # context = {
        # 'articleCategory': ArticleCategory.objects.all(),
        #     'articles': Article.objects.filter(category=category),
        # }
    elif request.method == 'OPTIONS':
        return JsonResponse({})