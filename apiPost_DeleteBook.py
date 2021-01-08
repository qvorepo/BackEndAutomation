import requests

import json
from utilities.resources import *
from utilities.configurations import *
from payLoad import *

url=getConfig()['API']['library_endpoint'] + ApiResources.addBook
addBook_response=requests.post(
    url,
    json=addBookPayload("kirw", "228"),
    headers={
            "Content-Type": "application/json"},
    )
addBookResponse_json = addBook_response.json()
print(addBook_response.json())
print (addBookResponse_json["Msg"])
print (addBookResponse_json["ID"])
assert addBook_response.status_code == 200

bookId = addBookResponse_json["ID"]

#Delete Book
url2=getConfig()['API']['library_endpoint'] + ApiResources.deleteBook
deleteBook_response = requests.post(
    url2,
    json={
        "ID": bookId},
    headers={
            "Content-Type": "application/json"},
    )
delBookResponse_json = deleteBook_response.json()
print(delBookResponse_json)
assert deleteBook_response.status_code == 200
assert delBookResponse_json["msg"] == "book is successfully deleted"

