import requests
import json
from Common import common
headers = common.headers


def create_role():
    url = "https://test.igancao.cn:8000/gateway/base/role/create"
    data = {
            "name": "测试权限",
            "permissionIds": "1,6,27,48,50,7,28,52,53,8,29,55,56,160,161,114,118,119,135,136,137,138,147,148,183,184,185,188,189,2,12,33,13,34,58,16,37,17,38,171,172,173,174,113,24,45,90,115,116,149,150,162,163,164,165,166,167,168,186,187,3,18,39,63,19,40,68,20,41,73,21,42,78,141,142,143,175,176,177,180,181,182,4,22,43,82,23,44,86,25,46,99,178,179,145,146,112,144,151,152,156,154,158,155,159,153,157"
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def delete_role(id):
    url = "https://test.igancao.cn:8000/gateway/base/role/delete"
    data = {
            "id": id
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def update_role(id):
    url = "https://test.igancao.cn:8000/gateway/base/role/update"
    data = {
            "name": "测试权限",
            "permissionIds": "1,6,27,48,50,7,28,52,53,8,29,55,56,160,161,114,118,119,135,136,137,138,147,148,183,184,185,188,189,2,12,33,13,34,58,16,37,17,38,171,172,173,174,113,24,45,90,115,116,149,150,162,163,164,165,166,167,168,186,187,3,18,39,63,19,40,68,20,41,73,21,42,78,141,142,143,175,176,177,180,181,182,4,22,43,82,23,44,86,25,46,99,178,179,145,146,112,144,151,152,156,154,158,155,159,153,157",
            "id": id
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()