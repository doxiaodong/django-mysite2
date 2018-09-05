# coding:utf-8

import urllib
import json
import requests
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from ..account.models import Profile

from django.shortcuts import render
from django.conf import settings

# Create your views here.


def github(request):
    if request.method == 'GET':
        get_data = request.GET
        step = get_data.get('step', 'code')
        if step == 'access_token':
            return get_access_token(request)
        elif step == 'user':
            return get_user(request)
        else:
            return get_code(request)


def get_code(request):
    if request.method == 'GET':
        url = settings.GITHUB_AUTHORIZE_URL
        data = {
            'client_id': settings.GITHUB_CLIENT_ID,
            'redirect_uri': 'https://api.darlin.me/third/github/?step=access_token',
            'state': 'd1f649dee27528d459001800fd88a8e9',
        }
        data = urllib.urlencode(data)
        redirect_url = url + '?' + data
        return HttpResponseRedirect(redirect_url)


def get_access_token(request):
    if request.method == 'GET':

        get_data = request.GET
        code = get_data.get('code')
        state = get_data.get('state')
        url = 'https://github.com/login/oauth/access_token'
        data = {
            'client_id': settings.GITHUB_CLIENT_ID,
            'client_secret': settings.GITHUB_CLIENT_SECRET,
            'code': code,
            'state': state,
        }
        data = urllib.urlencode(data)
        complete_url = url + '?' + data
        res = requests.post(complete_url)
        url_params = res.text
        return get_user(request, url_params)


def get_user(request, url_params):
    url = 'https://api.github.com/user'
    complete_url = url + '?' + url_params
    res = requests.get(complete_url)
    github_user_info = json.loads(res.text)

    user_info = {
        'username': '_github_' + github_user_info.get('login'),
        'email': github_user_info.get('email'),
        'nickname': github_user_info.get('login'),
        'pic': github_user_info.get('avatar_url'),
    }
    return github_login(request, user_info)


def github_login(request, data):
    r_username = data.get('username')
    r_email = data.get('email')
    r_nickname = data.get('nickname')
    r_pic = data.get('pic')

    if Profile.objects.filter(username=r_username):
        user = Profile.objects.get(username=r_username)
        user.nickname = r_nickname
        user.pic = r_pic
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
        new_user.third = 'github'
        new_user.save()

        i_user = authenticate(username=r_username, password=r_password)
        login(request, i_user)

    return HttpResponseRedirect('https://darlin.me')

