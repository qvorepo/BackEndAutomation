import requests
import json

se=requests.session()
se.cookies.update({'visit-month': 'February'})

cookie={'visit-year': '2021'}
response = se.get('http://httpbin.org/cookies', cookies=cookie)

json_response=response.json()
print(json_response)

assert response.status_code == 200
print("Response status code is {}".format(response.status_code) )