#!/usr/bin/python -tt
import requests
import json

payload = {'what': 'test_from_requests_module',
        'tags': 'deleteme, metoo', 'data': 'a nice automation test'}

post_request = requests.post('http://10.90.0.128/events/', data=json.dumps(payload))
print(post_request.text)
