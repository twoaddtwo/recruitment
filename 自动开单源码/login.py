import requests
import json

login_url = "https://test.igancao.cn:8000/gateway/base/employee/login"
login_headers = {"content-type": "application/json", "access_shop": "231", "access_version": "development"}


def login():
    login_data = {"type": "2", "passport": "yingzheng", "password": "123123qaz"}
    r = requests.post(login_url, headers=login_headers, data=json.dumps(login_data), verify=False)
    print(r.json()['data']['token'])
    return r.json()['data']['token']

token = login()
headers = {"content-type": "application/json", "access_shop": "231", "access_version": "development", "access_token": token}