import json
import requests
from Common import common
from DB import DB


def create_schedule(now):
    url = "https://test.igancao.cn:8000/gateway/treatment/schedule/create"
    data = {
            "canBook": "100",
            "classId": 227,
            "doctorId": 294,
            "weekly": "false",
            "roomId": 179,
            "scheduleDate": now,
            "scheduleTimeStart": "04:30",
            "scheduleTimeEnd": "06:45",
            "shopId": 199,
            "total": "100",
            "treatmentType": 1
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def update_schedule(id, now):
    url = "https://test.igancao.cn:8000/gateway/treatment/schedule/modify"
    data = {
            "canBook": "200",
            "classId": 227,
            "doctorId": 294,
            "weekly": "false",
            "roomId": 179,
            "scheduleDate": now,
            "scheduleTimeStart": "04:30",
            "scheduleTimeEnd": "06:45",
            "shopId": 199,
            "total": "200",
            "treatmentType": 1,
            "id": id
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def cancel_schedule(id):
    url = "https://test.igancao.cn:8000/gateway/treatment/schedule/cancel"
    data = {
            "id": id,
            "cancelWeekly": "false"
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def query_schedule_id(now):
    query_schedule_id_sql = "select id from gd_default.treatment_doctor_schedule where class_id = 227 and room_id = 179 and doctor_id = 294 and schedule_date = '%s'" % now
    print(query_schedule_id_sql)
    result, results = DB.exe_sql(query_schedule_id_sql)
    return result, results
