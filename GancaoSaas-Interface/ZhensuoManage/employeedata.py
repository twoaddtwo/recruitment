from Common import common
import requests
import json


def create_employee(phone, authcode):
    url = "https://test.igancao.cn:8000/gateway/base/employee/create"
    headers = common.headers
    data = {
        "name": "唐老鸭" + authcode,
        "phone": phone,
        "positionId": 2,
        "remark": "",
        "roleIds": "198",
        "sex": 1,
        "isDoctor": 0,
        "title": "",
        "introduction": "",
        "special": "",
        "disease": "",
        "avatar": "https://storage.test.igancao.cn/avatar/202103/1615360004084.JPG",
        "passport": "tanglaoya" + authcode
    }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(r.json())

