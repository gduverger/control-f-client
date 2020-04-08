import os
import logging
import requests

token = os.getenv('CTRLF_API_TOKEN')

def food(text, prefix=None, replace=None, suffix=None, token=None):

	json = {
		'text': text,
		'prefix': prefix,
		'replace': replace,
		'suffix': suffix
	}

	headers = {'Authorization': 'Bearer {}'.format(token or os.getenv('CTRLF_API_TOKEN'))}
	return requests.get('https://ctrlf-prod.herokuapp.com/food', json=json, headers=headers)
