import requests
from src.configs import config
from src.configs.payloads import payload as payl
import json
from dataclasses import dataclass
from src.helpers import helpers
__author__ = "Shubham Pimple"


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class ReqUtils(object):
    def __init__(self):
        self.base_url = config.API_HOSTS['test']

    def get(self, endpoint, headers=None):
        if not headers:
            headers = {'Content-Type': 'application/json'}
        url = self.base_url + endpoint
        rs_api = requests.get(url=url)
        return self.__get_responses(rs_api)

    def post(self, endpoint, headers=None, **kwargs):
        if not headers:
            headers = {'Content-Type': 'application/json'}
        url = self.base_url + endpoint
        print(json.dumps(payl))
        rs_api = requests.post(url=url, data=json.dumps(payl), headers=headers)
        return self.__get_responses(rs_api)

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text
        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}
        headers = response.headers

        return Response(
            status_code, text, as_dict, headers
        )





