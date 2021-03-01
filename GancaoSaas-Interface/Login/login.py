import requests
import json
headers = {"content-type": "application/json", "access_shop": "199", "access_version": "development"}
data = {"type": "2", "passport": "xiaowen", "password": "123123qaz"}
r = requests.post("https://test.igancao.cn:8000/gateway/base/employee/login", headers=headers, data=json.dumps(data), verify=False)
print("ssssssssssssssssss")
print(r.json()['data']['token'])


