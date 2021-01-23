import requests
import json

response = requests.get('https://reqres.in/api/users',
                        params={"id": 2},)
# print(response.text)
# print(type(response.text))
# dict_response=json.loads(response.text)
# print(dict_response["data"]["avatar"])
json_response=response.json()
print(json_response)
print(json_response["data"]["id"])
print(json_response["data"]["email"])

assert response.status_code == 200
print("Response status code is 200")
assert response.headers["Content-Type"] == 'application/json; charset=utf-8'
print("Response.headers Content-Type is 'application/json; charset=utf-8'")