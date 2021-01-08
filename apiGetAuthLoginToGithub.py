import requests
import json
from utilities.resources import *
from utilities.configurations import *

url=getConfig()['API']['github_endpoint'] + ApiResouces.githubLogin
print(url)

response=requests.get(url,auth=('qtvo91@yahoo.com',getGitHubPassword()))
response_json = response.json()
assert response.status_code == 200 #This did not work, 12/19/2020
print(response_json)


