import urllib
import urllib2

from django.shortcuts import render
from django.conf import settings

# Create your views here.

def get_code(request):
    url = settings.GITHUB_AUTHORIZE_URL
    data = {
        'client_id': settings.GITHUB_CLIENT_ID,
        'redirect_uri': settings.GITHUB_CALLBACK,
        'state': 'd1f649dee27528d459001800fd88a8e9',
		}
    data = urllib.urlencode(data)
    req = urllib2.Request(url, data, headers={'Accept': 'application/json'})
    response = urllib2.urlopen(req)
    result = response.read()
    print result
    return result
