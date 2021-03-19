import requests
import json
from Common import common
from DB import DB

headers = common.headers


def create_treatmentmode(title):
    url = "https://test.igancao.cn:8000/gateway/treatment/config/updateTreatmentTakeMode"
    data = {
            "detail": "",
            "id": "",
            "producePrice": "",
            "shopId": "",
            "title": title
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()

def update_treatmentmode(id):
    url = "https://test.igancao.cn:8000/gateway/treatment/config/updateTreatmentTakeMode"
    data = {
            "detail": "",
            "id": id,
            "producePrice": 0,
            "shopId": 199,
            "title": "修改测试"
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def create_medication_frequency(id):
    url = "https://test.igancao.cn:8000/gateway/treatment/config/updateTreatmentTakeMode"
    data = {
            "detail": "[{\"item\":\"一天3次\"},{\"item\":\"一天100次\"}]",
            "id": id,
            "producePrice": 0,
            "shopId": 199,
            "title": "修改测试"
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def update_medication_frequency(id):
    url = "https://test.igancao.cn:8000/gateway/treatment/config/updateTreatmentTakeMode"
    data = {
            "detail": "[{\"item\":\"一天3次s\"},{\"item\":\"sss\"}]",
            "id": id,
            "producePrice": 0,
            "shopId": 199,
            "title": "修改测试"
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def query_treatmentmode_id(title):
    query_treatmentmode_id_sql = "select id from gd_default.treatment_take_mode where title = '%s'" % title
    result, results = DB.exe_sql(query_treatmentmode_id_sql)
    return result, results


def create_class():
    url = "https://test.igancao.cn:8000/gateway/treatment/class/create"
    data = {
            "start": "00:45",
            "id": "",
            "name": "添加班次",
            "shopId": "",
            "end": "01:00"
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def update_class(id):
    url = "https://test.igancao.cn:8000/gateway/treatment/class/modify"
    data = {
            "start": "00:45",
            "id": id,
            "name": "修改班次",
            "shopId": "",
            "end": "01:00"
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def delete_class(id):
    url = "https://test.igancao.cn:8000/gateway/treatment/class/deleteClass"
    data = {
            "id": id
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def config_appointment(days):
    url = "https://test.igancao.cn:8000/gateway/treatment/config/saveCommonConfig"
    data = {
            "config": "ADVANCED_APPOINTMENT_DAYS",
            "configValue": days
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def config_register_order_auto_cancel(days):
    url = "https://test.igancao.cn:8000/gateway/treatment/config/saveCommonConfig"
    data = {
            "config": "REGISTER_ORDER_AUTO_CANCEL_DAYS",
            "configValue": days
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def config_unpaid_order_auto_cancel(days):
    url = "https://test.igancao.cn:8000/gateway/treatment/config/saveCommonConfig"
    data = {
            "config": "UNPAID_ORDER_AUTO_CLOSE_DAYS",
            "configValue": days
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def config_paymode():
    url = "https://test.igancao.cn:8000/gateway/pay/orderPay/savePayMode"
    data = {
            "payModeList": ["1", "5", "6", "7", "2", "3", "4"],
            "shopId": 199,
            "tenantKey": "test"
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def get_cloud_pharmacy_configlist():
    url = "https://test.igancao.cn:8000/gateway/supplychain/config/getCloucPharmacyConfigList"
    r = requests.post(url, headers=headers)
    return r.json()


def update_cloud_pharmacy_config(data):
    url = "https://test.igancao.cn:8000/gateway/supplychain/config/updateCloucPharmacyConfig"
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def update_sysinfo():
    url = "https://test.igancao.cn:8000/gateway/base/config/updateSysInfo"
    data = {
            "address": "聚公路16号",
            "name": "甘草测试中医诊所1",
            "phone": "14512223111",
            "shopName": "保和堂",
            "shopType": "MANY"
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def create_membercard_type(title):
    url = "https://test.igancao.cn:8000/gateway/crm/memberConfig/createMemberCardType"
    data = {
            "discount": 10,
            "enabled": "",
            "id": "",
            "numLimit": 10,
            "shopId": "",
            "title": title
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def query_membercard_id(title):
    query_membercard_id_sql = "select id from gd_default.crm_member_card_type where title = '%s'" % title
    result, results = DB.exe_sql(query_membercard_id_sql)
    return result, results


def update_membercard_type(id, title):
    url = "https://test.igancao.cn:8000/gateway/crm/memberConfig/modifyMemberCardType"
    data = {
            "discount": 10,
            "enabled": "",
            "id": id,
            "numLimit": 10,
            "shopId": "",
            "title": "小龙金卡修改" + title
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def stop_membercard_type(id):
    url = "https://test.igancao.cn:8000/gateway/crm/memberConfig/setMemberCardTypeStatus"
    data = {
            "id": id,
            "enabled": "false"
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def config_membercard():
    url = "https://test.igancao.cn:8000/gateway/crm/memberConfig/saveMemberCardConfig"
    data = {
            "id": 5,
            "length": 20,
            "prefix": "ghh",
            "start": 2,
            "shopId": ""
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def create_dock():
    url = "https://test.igancao.cn:8000/gateway/treatment/treatmentDocking/creatDockingInfo"
    data = {
            "checkCode": "00",
            "clientCode": "00",
            "mechanismCode": "00",
            "dosageId": 1,
            "type": "1",
            "id": ""
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def update_dock(id):
    url = "https://test.igancao.cn:8000/gateway/treatment/treatmentDocking/updateDockingInfo"
    data = {
            "checkCode": "001",
            "clientCode": "001",
            "mechanismCode": "001",
            "dosageId": 27,
            "type": 1,
            "id": id
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def delete_dock(id):
    url = "https://test.igancao.cn:8000/gateway/treatment/treatmentDocking/delDockingInfo"
    data = {"id": id}
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


