import requests
from behave import *
from payload import *
from utilities.resources import *
from utilities.configurations import *

@given('the Book details which needs to be added to Library')
def step_impl(context):
    #
    context.url = getConfig()['API']['library_endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload("merc","006");

@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )

@then('book is successfully added')
def step_impl(context):
    response_json = context.response.json()
    print(response_json)
    context.bookId = response_json['ID']
    print(context.bookId)
    assert response_json["Msg"] == "successfully added"

@given('the Book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.url = getConfig()['API']['library_endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload(isbn, aisle);

@then('status code of response should be {statusCode:d}') #statusCode is an integer.  Hence, d is present.
def step_impl(context,statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode

@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('qtvo91@yahoo.com', getGitHubPassword())

@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(getConfig()['API']['github_endpoint'] + ApiResources.githubRepos)
