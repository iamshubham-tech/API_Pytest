import openpyxl

from src.utils.RequestUtils import ReqUtils
from src.utils.fileReader import read_excel_file
import openpyxl
from src.configs import config
from src.helpers import helpers
from src.utils import getRepoURLs
import json


req = ReqUtils()


def test_get_user():
    response = req.get('/api/unknown/4')
    print(response)


def test_get_single_user():
    response = req.get('/api/users/2')
    print(response.text)

# def test_read_excel():
#     load = read_excel_file('data.xlsx')
#     sh = load['Sheet1']
#     print(sh.max_row)




