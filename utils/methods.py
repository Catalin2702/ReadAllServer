import json

import requests


def default(kwargs):
	print(kwargs)
	return {}


def api_service(kwargs):
	url = kwargs.get('url')
	action = kwargs.get('action')
	request = kwargs.get('api_request_map').get(action)
	data = {
		'query': kwargs.get('query'),
		'content_type': kwargs.get('content_type'),
	}
	if url and action and request and all(item for item in data.items()):
		url_request = url + request + '&'.join([f"{key}={value}" for key, value in data.items()])
		response = requests.get(url_request)
		return {'results': response.text} if response.status_code == 200 else {}
	return {}


def sign_in(kwargs):
	account = kwargs['account'](kwargs)
	logged = account.sign_in()
	response = {
		'signIn': {
			'email': account.get_email() if logged else '',
			'username': account.get_username() if logged else '',
			'token': account.get_token() if logged else '',
			'logged': logged
		}
	}
	return response


def register(kwargs):
	pass
