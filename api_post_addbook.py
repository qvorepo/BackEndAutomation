import requests

import json
from utilities.resources import *
from utilities.configurations import *

url=getConfig()['API']['library_endpoint'] + ApiResources.addBook
addBook_response=requests.post(
    url,
    json={
        "name": "Learn Appium Automation with Java",
        "isbn": "crpg",
        "aisle": "228",
        "author": "Jen Doe"},
    headers={
            "Content-Type": "application/json"},
    )
res_json = addBook_response.json()
print(addBook_response.json())
print (res_json["Msg"])
print (res_json["ID"])
assert addBook_response.status_code == 200

