import requests
import json


#http://rahulshettyacedemy.com
#visit-month

cookie={'visit-month': 'November'}
response = requests.get('http://rahulshettyacademy.com', cookies=cookie)



json_response=response.json()
print(json_response)


assert response.status_code == 200
print("Response status code is 200")
