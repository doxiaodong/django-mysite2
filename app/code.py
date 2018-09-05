import uuid
from django.http import JsonResponse as json_response, HttpResponse as http_response

Code = {
	'USER_IS_EXIST': {
		'code': 400001,
		'en': 'the user is exist'
	},

	'INVALID_USERNAME': {
		'code': 400002,
		'en': 'the username begin with _ is not allowed'
	},

	'INVALID_USERNAME_OR_PASSWORD': {
		'code': 400003,
		'en': 'invalid username or password'
	},

	'USER_IS_NOT_EXIST': {
		'code': 400004,
		'en': 'the use is not exist'
	},

	'CANNOT_MODIFY_THIRD': {
		'code': 400005,
		'en': 'modify the third is not allowed'
	},

	'USER_IS_NOT_ACTIVED': {
		'code': 400006,
		'en': 'the uer is not actived'
	},

	'NOT_ALLOWED': {
		'code': 400007,
		'en': 'not allowed'
	},

	'NOT_ALLOWED_NULL_REPLY': {
		'code': 400008,
		'en': 'not allowed null reply'
	},

	'LOGIN_FIRST': {
		'code': 401001,
		'en': 'login first'
	},

	'SERVER_ERROR': {
		'code': 50001,
		'en': 'server error'
	},
}

def gen_traceid():
	return uuid.uuid4()

def HttpResponse(data, **kwargs):
	ret = http_response(data, **kwargs)
	ret['traceid'] = gen_traceid()
	return ret

def JsonResponse(data, **kwargs):
	ret = json_response(data, **kwargs)
	ret['traceid'] = gen_traceid()
	return ret

def errorResponse(key, code=None):
	res = Code[key]
	if res == None:
		return JsonResponse({
			'error': 'error is not defined, check backend'
		}, status=500)

	if code == None:
		code = res['code']/1000

	return JsonResponse(res, status=code)
