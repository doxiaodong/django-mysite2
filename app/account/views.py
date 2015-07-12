# coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..account.models import Profile
from ..comments.models import SubComment
from PIL import Image
from django.conf import settings
import os
from django.utils import timezone

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
def register(request):
    if request.method == "POST":
        post_data = request['POST']

        r_username = post_data.get('username', None)
        if Profile.objects.filter(username=r_username):
            return JsonResponse({'status': False, 'data': {'error': '用户名已经存在'}})
        else:
            r_email = post_data.get('email', None)
            r_password = post_data.get('password', None)
            r_firstname = post_data.get('firstname', None)
            r_lastname = post_data.get('lastname', None)

            # create_user(username, email=None, password=None, **extra_fields)
            new_user = Profile.objects.create_user(
                username=r_username,
                email=r_email,
                password=r_password,
            )

            if r_firstname:
                new_user.first_name = r_firstname
            else:
                new_user.first_name = r_username

            new_user.last_name = r_lastname

            new_user.save()

            i_user = authenticate(username=r_username, password=r_password)
            login(request, i_user)
            respose = {'status': True, 'data': {'nickname': i_user.nickname}}
            return JsonResponse(respose)


def signin(request):
    if request.method == "POST":
        post_data = request.POST

        username = post_data.get('username', None)
        password = post_data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                respose = {'status': True, 'data': {'nickname': user.nickname}}
                return JsonResponse(respose)
            else:
                pass
        else:
            respose = {'status': False, 'data': {'error': '用户名或密码错误！'}}
            return JsonResponse(respose)


def signout(request):
    if request.method == "POST":
        logout(request)
        respose = {'status': True, 'data': {}}
        return JsonResponse(respose)