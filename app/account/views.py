# coding:utf-8
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from ..account.models import Profile
from ..comments.models import SubComment
from PIL import Image
from django.conf import settings
import os
from django.utils import timezone

from api.views import get_user_info

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# functions


def clip_resize_img(ori_img, dst_w, dst_h):
    im = Image.open(ori_img)
    ori_w, ori_h = im.size

    dst_scale = float(dst_h) / dst_w  # 目标高宽比
    ori_scale = float(ori_h) / ori_w  # 原高宽比
    if ori_scale >= dst_scale:
        # 过高
        width = ori_w
        height = int(width * dst_scale)

        ww = dst_w

    else:
        # 过宽
        height = ori_h
        width = int(height * dst_scale)

        ww = int(100 / ori_scale)

    dst_w = ww

    new_im = im

    ratio = float(dst_w) / width
    new_width = int(width * ratio)
    if ori_w < new_width:
        new_width = ori_w

    new_height = int(height * ratio)
    if ori_h < new_height:
        new_height = ori_h

    new_im.thumbnail((new_width, new_height), Image.ANTIALIAS)
    return new_im


# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        post_data = request.POST

        r_username = post_data.get('username', None)
        if Profile.objects.filter(username=r_username):
            return JsonResponse({'status': 0, 'msg': '用户名已经存在', 'data': {}})
        else:
            r_email = post_data.get('email', None)
            r_password = post_data.get('password', None)
            r_nickname = post_data.get('nickname', None)

            # create_user(username, email=None, password=None, **extra_fields)
            new_user = Profile.objects.create_user(
                username=r_username,
                email=r_email,
                password=r_password,
            )

            if r_nickname:
                new_user.nickname = r_nickname
            else:
                new_user.nickname = r_username

            new_user.save()

            i_user = authenticate(username=r_username, password=r_password)
            login(request, i_user)
            respose = {
                'status': 1,
                'msg': '注册成功',
                'data': {
                    'user': get_user_info(i_user)
                }
            }
            return JsonResponse(respose)


@csrf_exempt
def signin(request):
    if request.method == "POST":
        post_data = request.POST
        username = post_data.get('username', None)
        password = post_data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                respose = {
                    'status': 1,
                    'msg': '登录成功',
                    'data': {
                        'user': get_user_info(user)
                    }
                }
                return JsonResponse(respose)
            else:
                pass
        else:
            respose = {'status': 0, 'msg': '用户名或密码错误', 'data': {}}
            return JsonResponse(respose)


@ensure_csrf_cookie
@csrf_exempt
def signout(request):
    if request.method == "POST":
        logout(request)
        respose = {'status': 1, 'msg': '注销成功', 'data': {}}
        return JsonResponse(respose)


@csrf_exempt
def get_user(request):
    if request.method == "GET":
        get_data = request.GET
        user = Profile.objects.get(username=get_data.get('username', None))
        if user:
            respose = {
                'status': 1,
                'msg': '获取用户信息成功',
                'data': {
                    'user': get_user_info(user)
                }
            }
        else:
            respose = {
                'status': 0,
                'msg': '用户不存在',
                'data': {}
            }
        return JsonResponse(respose)

@csrf_exempt
def setting(request):
    if request.method == "PUT":
        put_data = request.PUT
        print(put_data)

        s_username = put_data.get('username', None)

        if s_username != request.user.username and Profile.objects.filter(username=s_username):
            return JsonResponse({'status': 0, 'msg': '用户名已经存在', 'data': {}})
        else:
            s_email = put_data.get('email', None)
            s_nickname = put_data.get('nickname', None)
            s_sex = put_data.get('sex', None)
            s_pic = request.FILES.get('pic', None)

            s_user = Profile.objects.get(username=request.user.username)

            if s_pic:
                n_s_pic = clip_resize_img(s_pic, 100, 100)

                url = 'user/' + s_pic.name
                name = settings.MEDIA_ROOT + '/' + url
                if os.path.exists(name):
                    file, ext = os.path.splitext(s_pic.name)
                    file += (timezone.now().strftime("%Y-%m-%d_%H_%s"))
                    s_pic.name = file + ext
                    url = 'user/' + s_pic.name
                    name = settings.MEDIA_ROOT + '/' + url
                n_s_pic.save(name)

                s_user.pic = url
            if s_username:
                s_user.username = s_username
            if s_email:
                s_user.email = s_email
            if s_nickname:
                s_user.nickname = s_nickname
            s_user.sex = s_sex

            s_user.save()

            respose = {
                'status': 1,
                'msg': '修改成功',
                'data': {}
            }
            return JsonResponse(respose)