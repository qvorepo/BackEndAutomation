from payLoad import *

import requests
import json
import configparser
from utilities.configurations import *
from utilities.resources import *

url=getConfig()['API']['endpoint']+ ApiResources.apiUser
response=requests.post(url,json=

addUser("Cindy", "SDET"), headers={"Content-Type": "application/json"}


)
response_json = response.json()
#assert response.status_code == 201
print(response.status_code)
print(response_json)


