# coding:utf-8

from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from django.views.decorators.csrf import get_token


# Create your views here.
@ensure_csrf_cookie
def init_homepage(request):

    if request.method == "GET":

        respose = {
            'status': 1,
            'msg': '请求csrftoken, sessionid成功',
            'data': {
                'csrftoken': get_token(request)
            }
        }
        return JsonResponse(respose)