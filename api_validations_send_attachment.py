import requests
import json

url='https://httpbin.org/post'
files={'files': open('C:\\Users\\Mamga\\Downloads\\ErrorCounts_Transformed.xlsx', 'rb')}

response = requests.post(url,files=files)

json_response=response.json()
print(json_response)

assert response.status_code == 200
print("Response status code is {}".format(response.status_code) )
print('The test passed!  A file was attached successfully in the POST request!')