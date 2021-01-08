import requests
import json
from utilities.resources import *
from utilities.configurations import *

se=requests.sessions()
se.auth=auth=('qtvo91@yahoo.com',getGitHubPassword())

url=getConfig()['API']['github_endpoint'] + ApiResouces.githubRepos
print(url)

response=se.get(url)
response_json = response.json()
assert response.status_code == 200 #This did not work, 12/19/2020
print(response_json)


