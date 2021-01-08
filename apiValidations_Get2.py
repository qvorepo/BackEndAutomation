import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/users/1/albums',
                        params=None,)
# print(response.text)
# print(type(response.text))
# dict_response=json.loads(response.text)
# print(dict_response["data"]["avatar"])
json_response=response.json()
print(json_response)

assert response.status_code == 200
print("Response status code is 200")
assert response.headers["Content-Type"] == 'application/json; charset=utf-8'
print("Response.headers Content-Type is 'application/json; charset=utf-8'")
for actualUser in json_response:
    if actualUser["title"] == 'qui fuga est a eum':
        print(actualUser["userId"])
        print(actualUser["id"])
        print(actualUser)
        break
expectedUser ={'userId': 1, 'id': 8, 'title': 'qui fuga est a eum'}

assert actualUser == expectedUser


