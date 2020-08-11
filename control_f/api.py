import os
import logging
import requests

API_URL = os.getenv('CONTROL_F_API_URL', 'https://ctrlf-prod.herokuapp.com/food')
API_KEY = os.getenv('CONTROL_F_API_KEY')

def food(text, prefix=None, replace=None, suffix=None, token=None):

	json = {
		'text': text,
		'prefix': prefix,
		'replace': replace,
		'suffix': suffix
	}

	headers = {'Authorization': 'Bearer {}'.format(token or API_KEY)}
	return requests.get(API_URL, json=json, headers=headers)
