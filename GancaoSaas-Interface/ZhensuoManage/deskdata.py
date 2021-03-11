import requests
import json
from Common import common
from DB import DB

headers = common.headers


def create_desk(code):
    url = "https://test.igancao.cn:8000/gateway/base/desk/create"
    data = {
            "code": code,
            "title": "科室" + str(code)
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def update_desk(code, id):
    url = "https://test.igancao.cn:8000/gateway/base/desk/update"
    data = {
            "code": code,
            "title": "科室" + str(code),
            "id": id
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def disable_desk(id, enable):
    url = "https://test.igancao.cn:8000/gateway/base/desk/disable"
    data = {
            "id": id,
            "enable": enable
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def create_room(code, deskid):
    url = "https://test.igancao.cn:8000/gateway/base/room/create"
    data = {
            "code": code,
            "title": "诊室" + str(code),
            "remark": "sd",
            "deskId": deskid
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def update_room(code, roomid):
    url = "https://test.igancao.cn:8000/gateway/base/room/update"
    data = {
            "code": code,
            "title": "修改诊室" + str(code),
            "id": roomid,
            "remark": "\"修改诊室\""}
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def disable_room(roomid, enable):
    url = "https://test.igancao.cn:8000/gateway/base/room/disable"
    data = {
            "id": roomid,
            "enable": enable
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def query_deskid(code):
    query_deskid_sql = "select id from gd_default.base_desk where code = '%s'" % code
    result, results = DB.exe_sql(query_deskid_sql)
    return result, results


def query_roomid(code):
    query_roomid_sql = "select id from gd_default.base_room where code = '%s'" % code
    result, results = DB.exe_sql(query_roomid_sql)
    return result, results

