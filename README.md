# API_Pytest
**Author : Shubham Pimple**

This project is about automation of API's using PyTest framework. So far I have covered reqres and GIT API requests.
Many more wil get added to this project

#Libraries needed
- Requests
- Pytest
- JSON
- Allure

#**Running tests with Allure report:**

pytest 'path to the file/files' --alluredir 'path of the folder in which reports will get stored' 

If you want to automate git api's then you need to creat personal access token first from your git account


**#Framework contains**

Utils :- 
- getRepoURLs : To get diffrent URL's for GET and POST for GIT API
- GITRequestUtils : Contains API methods for GIT
- RequestUtils : Contains API Methods for reqres.in free API

Configs :- 
- config.py : Contains Auth data and usernames
- payload.py : Contains payload to be send in methods

helpers :- 
- helpers.py : Contains json response validation methods



