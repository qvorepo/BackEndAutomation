import requests
import json
from utilities.resources import *
from utilities.configurations import *

url=getConfig()['API']['endpoint'] + ApiResources.apiLogin

response=requests.post(url, json= { "email": "eve.holt@reqres.in", "password": "cityslicka" },
                       headers={"Content-Type": "application/json"} )
response_json = response.json()
assert response.status_code == 200
print(response_json)
print(response_json["token"])

