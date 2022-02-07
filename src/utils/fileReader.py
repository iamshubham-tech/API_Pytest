import json
from pathlib import Path
import openpyxl


BASE_PATH = Path.cwd().joinpath('data')


def get_file_with_json_ext(file_name):
    if '.json' in file_name:
        path = BASE_PATH.joinpath(file_name)
    elif '.xlsx' in file_name:
        path = BASE_PATH.joinpath(f'{file_name}.json')
    return path


def get_file_with_xlsx_extension(file_name):
    if '.xlsx' in file_name:
        path = BASE_PATH.joinpath(file_name)
    else:
        path = BASE_PATH.joinpath(f'{file_name}.xlsx')
    return path


def read_json_file(file_name):
    path = get_file_with_json_ext(file_name)
    with path.open(mode='r') as f:
        return json.load(f)


def read_excel_file(file_name):
    path = get_file_with_xlsx_extension(file_name)
    print(path)
    load = openpyxl.load_workbook(path)
    return load



