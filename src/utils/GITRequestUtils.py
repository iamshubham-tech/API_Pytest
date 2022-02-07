"""
This file is used for GIT Repo requests methods
"""
__author__ = "Shubham Pimple"

from src.utils import getRepoURLs
import requests
from src.configs.config import Auth_data
import json
from src.configs.payloads import repo_details
from src.helpers.helpers import validate_content_from_repo


class GitRequestUtils(object):

    def __init__(self):
        self.BASE_URL = getRepoURLs.BASE_URL
        self.USERNAME = getRepoURLs.USERNAME
        self.REPO_NAME = getRepoURLs.REPO_NAME
        self.REPO_DETAILS = getRepoURLs.repo_details

    def get_repos(self,headers=None):
        if headers is None:
            headers = {
                'Content-Type' : 'application/json'
            }
        url = getRepoURLs.repos_url(self.USERNAME)
        resp = requests.get(url=url, headers=headers)
        return resp

    def get_single_repo_info(self, headers=None):
        if headers is None:
            headers = {
                'Content-Type' : 'application/json'
            }
        url = getRepoURLs.single_repo_url(self.USERNAME,self.REPO_NAME)
        print(url)
        resp = requests.get(url=url, headers=headers)
        return resp

    def post_repo(self, headers=None):
        if headers is None:
            headers = {
                'Content-Type': 'application/json'
            }
        url = getRepoURLs.post_repo_url()
        resp = requests.post(url=url,data=json.dumps(self.REPO_DETAILS), headers=Auth_data)
        return resp

    """
    The below method will be used whenever there are straightforward endpoints
    """
    def get(self, endpoint, headers=None):
        if headers is None:
            headers = {
                'Content-Type': 'application/json'
            }
        url = self.BASE_URL + "/" + endpoint
        resp = requests.get(url=url, headers=headers)
        return resp

    def delete(self, endpoint, headers=None):
        if headers is None:
            headers = {
                'Content-Type': 'application/json'
            }
        url = self.BASE_URL + endpoint
        resp = requests.delete(url=url,headers=Auth_data)
        return resp

    def post(self, endpoint, data, headers=None):
        if headers is None:
            headers = {
                'Content-Type': 'application/json'
            }
        headers = Auth_data
        url = self.BASE_URL + endpoint
        resp = requests.post(url=url, data=data, headers=headers)
        return resp

