# coding:utf-8

import json
import requests
from urllib import parse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from ..account.models import Profile

from django.shortcuts import render
from django.conf import settings


def login_route(request):
    if request.method == 'GET':
        get_data = request.GET
        step = get_data.get('step', 'code')
        if step == 'access_token':
            return get_access_token(request)
        elif step == 'user_openid':
            return get_user_openid(request)
        else:
            return get_code(request)


def get_code(request):
    if request.method == 'GET':
        url = settings.QQ_AUTHORIZE_URL
        data = {
            'response_type': 'code',
            'client_id': settings.QQ_CLIENT_ID,
            'redirect_uri': 'https://api.darlin.me/third/qq/?step=access_token',
            'state': 'd1f649dee27528d459001800fd88a8e9',
        }
        data = parse.urlencode(data)
        redirect_url = url + '?' + data
        return HttpResponseRedirect(redirect_url)


def get_access_token(request):
    if request.method == 'GET':

        get_data = request.GET
        code = get_data.get('code')
        # state = get_data.get('state')
        url = 'https://graph.qq.com/oauth2.0/token'
        data = {
            'grant_type': 'authorization_code',
            'client_id': settings.QQ_CLIENT_ID,
            'client_secret': settings.QQ_CLIENT_SECRET,
            'code': code,
            'redirect_uri': 'https://api.darlin.me/third/qq/?step=user_openid',
        }
        data = parse.urlencode(data)
        complete_url = url + '?' + data
        ret = requests.get(complete_url)
        access_token = parse.parse_qs(ret.text)['access_token'][0]
        return get_user_openid(request, access_token)


def get_user_openid(request, access_token):
    url = 'https://graph.qq.com/oauth2.0/me'
    data = {
        'access_token': access_token,
    }
    data = parse.urlencode(data)
    complete_url = url + '?' + data
    res = requests.get(complete_url)

    url_params = res.text
    return get_user(request, url_params, access_token)


def callback(obj):
    return obj


def get_user(request, url_params, access_token):
    # url_params = 'callback( {"client_id":"101322546","openid":"442F5423D8457D1C8DCF2B5D01023B25"} );'
    new_url_params = url_params.replace(';', '')
    ret = eval(new_url_params)
    url = 'https://graph.qq.com/user/get_user_info'
    data = {
        'access_token': access_token,
        'oauth_consumer_key': ret.get('client_id'),
        'openid': ret.get('openid'),
    }
    data = parse.urlencode(data)
    complete_url = url + '?' + data
    res = requests.get(complete_url)
    qq_user_info = json.loads(res.text)

    if qq_user_info.get('gender') == '男':
        sex = 0
    else:
        sex = 1
    user_info = {
        'username': '_qq_' + ret.get('openid'),
        'email': ret.get('openid')[0:10] + '@qq.com',
        'nickname': qq_user_info.get('nickname'),
        'pic': qq_user_info.get('figureurl_qq_2'),
        'sex': sex
    }
    return qq_login(request, user_info)


def qq_login(request, data):
    r_username = data.get('username')[0:25]
    r_nickname = data.get('nickname')
    r_email = data.get('email')
    r_pic = data.get('pic')
    r_sex = data.get('sex')

    if Profile.objects.filter(username=r_username):
        user = Profile.objects.get(username=r_username)
        user.nickname = r_nickname
        user.email = r_email
        user.pic = r_pic
        user.sex = r_sex
        user.save()

        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
    else:

        r_password = 'abcdefghijklmnopqrstuvwxyz'
        # create_user(username, email=None, password=None, **extra_fields)
        new_user = Profile.objects.create_user(
            username=r_username,
            email=r_email,
            password=r_password,
        )
        new_user.nickname = r_nickname
        new_user.pic = r_pic
        new_user.sex = r_sex
        new_user.third = 'qq'

        new_user.save()

        i_user = authenticate(username=r_username, password=r_password)
        login(request, i_user)

    return HttpResponseRedirect('https://darlin.me')
