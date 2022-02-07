import json


def validate_created_user(response):
    return 'id' in response


def is_repo_created(response):
    return 'id' in response


def validate_content_from_repo(response, login, name):
    json_response = response.json()
    owner = json_response['owner']
    if json_response['name'] == name and owner['login'] == login:
        print("Repo is successfully created and content is validated !!")





