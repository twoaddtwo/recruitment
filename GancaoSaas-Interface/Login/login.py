import requests
import json

login_url = "https://test.igancao.cn:8000/gateway/base/employee/login"
login_headers = {"content-type": "application/json", "access_shop": "199", "access_version": "development"}


def login():
    login_data = {"type": "2", "passport": "xiaowen", "password": "123123qaz"}
    r = requests.post(login_url, headers=login_headers, data=json.dumps(login_data), verify=False)
    print(r.json()['data']['token'])
    return r.json()['data']['token']

def send_authcode(phone):
    url = "https://test.igancao.cn:8000/gateway/base/sms/send_authcode"
    data = {"phone": phone, "action": "login"}
    r = requests.post(url, headers=login_headers, data=json.dumps(data), verify=False)
    print(r.json())


def authcode_login(phone, authcode):
    authcode_login_data = {"type": 1, "phone": phone, "authcode": authcode}
    r = requests.post(login_url, headers=login_headers, data=json.dumps(authcode_login_data), verify=False)
    print(r.json())
