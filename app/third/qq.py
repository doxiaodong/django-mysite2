import urllib
import json
import requests
import urlparse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
from ..account.models import Profile

from django.shortcuts import render
from django.conf import settings


def login(request):
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
        data = urllib.urlencode(data)
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
        data = urllib.urlencode(data)
        complete_url = url + '?' + data
        ret = requests.get(complete_url)
        access_token = urlparse.parse_qs(ret.text)['access_token'][0]
        return get_user_openid(request, access_token)


def get_user_openid(request, access_token):
    url = 'https://graph.qq.com/oauth2.0/me'
    data = {
        'access_token': access_token,
    }
    data = urllib.urlencode(data)
    complete_url = url + '?' + data
    res = requests.get(complete_url)

    url_params = res.text
    return get_user(request, url_params, access_token)


def callback(obj):
    print 111, obj
    return obj


def get_user(request, url_params, access_token):
    # url_params = 'callback( {"client_id":"101322546","openid":"442F5423D8457D1C8DCF2B5D01023B25"} );'
    url_params = url_params.strip[0:-1]
    print url_params
    ret = eval(url_params)
    print ret
    url = 'https://graph.qq.com/user/get_user_info'
    data = {
        'access_token': access_token,
        'oauth_consumer_key': ret.get('client_id'),
        'openid': ret.get('openid'),
    }
    data = urllib.urlencode(data)
    complete_url = url + '?' + data
    res = requests.get(complete_url)
    qq_user_info = json.loads(res.text)
    print 5555, qq_user_info

    user_info = {
        'username': 'qq_' + url_params['openid'],
        'email': '',
        'nickname': qq_user_info.get('nickname')
    }
    return qq_login(request, user_info)


def qq_login(request, data):
    print 'qq_login'
    r_username = data.get('username')
    if Profile.objects.filter(username=r_username):
        user = Profile.objects.get(username=r_username)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
    else:
        r_email = data.get('email')
        r_password = 'abcdefghijklmnopqrstuvwxyz'
        r_nickname = data.get('nickname')

        # create_user(username, email=None, password=None, **extra_fields)
        new_user = Profile.objects.create_user(
            username=r_username,
            email=r_email,
            password=r_password,
        )
        new_user.nickname = r_nickname
        new_user.third = 'qq'

        new_user.save()

        i_user = authenticate(username=r_username, password=r_password)
        login(request, i_user)

    print 66666

    return HttpResponseRedirect('https://darlin.me')
