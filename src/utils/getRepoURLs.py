"""
This code provide the urls for particular request
"""
__author__ = "Shubham Pimple"

from src.configs.config import API_HOSTS
from src.configs.payloads import repo_details


BASE_URL = "https://api.github.com"
USERNAME = API_HOSTS['username']
REPO_NAME = API_HOSTS['reponame']
REPO_DETAILS = repo_details


def repos_url(username):
    return BASE_URL+"/users/"+username+"/repos"


def single_repo_url(username, repo_name):
    return BASE_URL+"/repos/"+username+"/"+repo_name


def post_repo_url():
    return "https://api.github.com/user/repos"


def delete_repo_url(username, repo_name):
    return BASE_URL + "/repos/" + username + "/" + repo_name


def get_users():
    return BASE_URL + "/users"
