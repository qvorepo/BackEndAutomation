import requests
import json
import configparser
from utilities.configurations import *
from utilities.resources import *

url=getConfig()['API']['endpoint'] + ApiResources.apiUser
response=requests.post(url, json=

{"Name": "Lori Brown",
"Job" : "QA Analyst"
}, headers={"Content-Type": "application/json"}


)
response_json = response.json()
assert response.status_code == 201
print(response_json)
print(response_json["id"] +" " + response_json["Name"]  )
print (type(response_json))
