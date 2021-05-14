import json
import requests
from Common import common


def get_vipcard_num():
    url = "https://test.igancao.cn:8000/gateway/crm/member/generateCardNumber"
    r = requests.post(url, headers=common.headers, verify=False)
    return r.json()




def create_vipcard(cardnum, phone, patientnum, patientid):
    url = "https://test.igancao.cn:8000/gateway/crm/member/activateCard"
    data = {
            "memberCardNo": cardnum,
            "patientId": patientid,
            "medicalNumber": patientnum,
            "modifyPatient": "true",
            "name": phone,
            "phone": phone,
            "age": 10,
            "sex": 1,
            "typeId": 64,
            "chargedCapital": 1,
            "chargedGiftCash": 0,
            "payMode": 1
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def create_vipcard_tocharge(id):
    url = "https://test.igancao.cn:8000/gateway/crm/member/toCharge"
    data = {
            "id": id,
            "operatedCapital": 100,
            "operatedGiftCash": 100,
            "payMode": 1,
            "typeId": 64
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def create_vipcard_refund(id):
    url = "https://test.igancao.cn:8000/gateway/crm/member/refund"
    data = {
            "id": id,
            "operatedCapital": 1,
            "operatedGiftCash": 1,
            "payMode": 1,
            "cancel": "false"
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()

