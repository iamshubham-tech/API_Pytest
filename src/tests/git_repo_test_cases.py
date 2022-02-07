import requests
from _pytest import fixtures

from src.utils import getRepoURLs
import json
from src.utils import getRepoURLs
from src.utils.GITRequestUtils import GitRequestUtils
from src.helpers.helpers import is_repo_created
from src.configs.payloads import repo_details
from src.helpers.helpers import validate_content_from_repo
from src.configs.config import API_HOSTS
import pytest


req = GitRequestUtils()

"""
Get List of repos
"""
def test_get_repos():
    res = req.get_repos()
    print(res.json())


"""Create Repo"""
def test_create_repo():
    res = req.post_repo()
    print(res.json())
    is_created = is_repo_created(res.json())
    assert is_created is True
    validate_content_from_repo(res, API_HOSTS['username'], repo_details['name'])
    print('Successfully created !!!')


#Getting list of users
def test_get_users():
    res = req.get('users')
    print(res.json())


#Getting a specific user
def test_get_single_user():
    res = req.get('users/{}'.format(API_HOSTS['username']))
    print(res.json())


"""Deleting a repo"""
def test_delete_repo():
    res = req.delete('/repos/{}/{}'.format(API_HOSTS['username'],repo_details['name']))


"""Creating a repo by using post method directly"""
"""Note: Providing endpoints in the test file itself. Not using the defined method for repo creation"""
def test_repo_create():
    res = req.post('/user/repos', data=json.dumps(repo_details))
    print(res.status_code)




