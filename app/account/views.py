# coding:utf-8
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
from ..account.models import Profile
import hashlib
from django.conf import settings
from qiniu import Auth
from qiniu import put_data
import oss2

from api.views import get_user_info

from app.code import errorResponse

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# Create your views here.
# @csrf_exempt
def register(request):
    if request.method == "POST":
        post_data = request.POST

        r_username = post_data.get('username', None)
        if Profile.objects.filter(username=r_username):
            return errorResponse('USER_IS_EXIST')
        elif r_username[0] == '_':
            return errorResponse('INVALID_USERNAME')
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
                'user': get_user_info(i_user)
            }
            return JsonResponse(respose)


# @csrf_exempt
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
                    'user': get_user_info(user)
                }
                return JsonResponse(respose)
            else:
                pass
        else:
            return errorResponse('INVALID_USERNAME_OR_PASSWORD')


@ensure_csrf_cookie
# @csrf_exempt
def signout(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({})


# @csrf_exempt
def get_user(request):
    if request.method == "POST":
        post_data = request.POST
        user = Profile.objects.get(username=post_data.get('username', None))
        if user:
            respose = JsonResponse({
                'user': get_user_info(user)
            })
        else:
            respose = errorResponse('USER_IS_NOT_EXIST')
        return respose


# @csrf_exempt
def setting(request):
    if request.method == "POST":
        post_data = request.POST
        m = hashlib.md5()

        s_username = post_data.get('username', None)

        if s_username != request.user.username and Profile.objects.filter(username=s_username):
            return errorResponse('USER_IS_EXIST')
        if s_username != request.user.username and request.user.third != 'none':
            return errorResponse('CANNOT_MODIFY_THIRD')
        else:
            s_email = post_data.get('email', None)
            s_nickname = post_data.get('nickname', None)
            s_sex = post_data.get('sex', None)
            s_pic = request.FILES.get('pic', None)

            s_user = Profile.objects.get(username=request.user.username)

            # if s_pic:
            #     m.update(s_pic.name)
            #     pic_name_md5 = m.hexdigest()
            #     q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
            #     key = settings.QINIU_MEDIA_SRC + 'user/' + s_user.username + '/' + pic_name_md5
            #     data = s_pic
            #     token = q.upload_token(settings.QINIU_BUCKET_DEFAULT)
            #     ret, info = put_data(token, key, data, mime_type=s_pic.content_type)
            #     s_user.pic = ret['key']

            if s_pic:
                m.update(s_pic.name)
                pic_name_md5 = m.hexdigest()
                auth = oss2.Auth(settings.ALIYUN_KEY_ID, settings.ALIYUN_KEY_SECRET)
                bucket = oss2.Bucket(auth, settings.ALIYUN_BUCKET_ENDPOIONTS, settings.ALIYUN_BUCKET)
                key = settings.ALIYUN_MEDIA_SRC + 'user/' + s_user.username + '/' + pic_name_md5
                bucket.put_object(key, s_pic, {
                  'Content-Type': s_pic.content_type
                })
                s_user.pic = key

            if s_username:
                s_user.username = s_username
            if s_email:
                s_user.email = s_email
            if s_nickname:
                s_user.nickname = s_nickname
            s_user.sex = s_sex

            s_user.save()

            return JsonResponse({})


# @csrf_exempt
def change(request):
    if request.method == "POST":
        post_data = request.POST
        username = post_data.get('username', None)
        password1 = post_data.get('old_password', None)
        password2 = post_data.get('new_password', None)
        if password1 == '':
            password1 = 'abcdefghijklmnopqrstuvwxyz'
        user = authenticate(username=username, password=password1)
        if user is not None:
            if user.is_active:
                user.set_password(password2)
                user.save()
                login(request, user)
                respose = {
                    'user': get_user_info(user)
                }
                return JsonResponse(respose)
            else:
                return errorResponse('USER_IS_NOT_ACTIVED')
        else:
            return errorResponse('INVALID_USERNAME_OR_PASSWORD')


# @csrf_exempt
def reset(request):
    if request.method == "POST":
        if request.user.id == 1:
            post_data = request.POST
            username = post_data.get('username', None)
            password2 = post_data.get('new_password', None)
            user = Profile.objects.get(username=username)
            if user is not None:
                user.set_password(password2)
                user.save()
                respose = {
                    'user': username
                }
                return JsonResponse(respose)
            else:
                return errorResponse('USER_IS_NOT_EXIST')
        else:
            return errorResponse('NOT_ALLOWED')
