from Common import common
import requests
import json
from DB import DB

headers = common.headers


def create_employee(phone, authcode):
    url = "https://test.igancao.cn:8000/gateway/base/employee/create"
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
    return r.json(), r.json()['data']


def getlist_employee(phone):
    url = "https://test.igancao.cn:8000/gateway/base/employee/getList"
    data = {
            "pageNum": 1,
            "pageSize": 10,
            "enabledVals": "",
            "name": "",
            "phone": phone,
            "positionIds": "",
            "remark": "",
            "sex": ""
            }
    r = requests.post(url, headers= headers, data = json.dumps(data), verify=False)
    return r.json()


def update_employee(phone, authcode, id):
    url = "https://test.igancao.cn:8000/gateway/base/employee/update"
    data = {
            "name": "唐老鸭" + authcode,
            "phone": phone,
            "positionId": 2,
            "remark": "",
            "roleIds": "198",
            "sex": 1,
            "isDoctor": 1,
            "title": "医师",
            "introduction": "",
            "special": "",
            "disease": "",
            "avatar": "https://storage.test.igancao.cn/avatar/202103/1615360004084.JPG",
            "passport": "tanglaoya" + authcode,
            "id": id
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def disable_employee(id, enable):
    url = "https://test.igancao.cn:8000/gateway/base/employee/disable"
    data = {
            "id": id,
            "enable": enable
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def del_employee(id):
    del_employee_sql = "delete from gd_default.base_employee where id = '%s'" % id
    result = DB.del_sql(del_employee_sql)
    return result


def query_employee(id):
    query_employee_sql = "select * from gd_default.base_employee where id = '%s'" % id
    result = DB.exe_sql(query_employee_sql)
    return result
