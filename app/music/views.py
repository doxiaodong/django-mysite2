# coding:utf-8

import requests
from app.code import HttpResponse

def get_lyric_by_id(request, musicid):
	if request.method == 'GET':
		callback = request.GET.get('callback')
		url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric.fcg'
		data = {
			'musicid': musicid,
			'callback': callback,
		}
		headers = {
			'referer': 'https://y.qq.com/portal/player.html',
			# 'cookie': 'qqmusic_uin=12345678; qqmusic_key=12345678; qqmusic_fromtag=30',
		}
		ret = requests.get(url, params=data, headers=headers)
		return HttpResponse(ret.text, content_type ='application/javascript')
