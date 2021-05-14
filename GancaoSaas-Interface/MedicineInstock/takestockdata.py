import json
import requests
from Common import common


def create_medicine_takestock():
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineTakestock/takestockCreate"
    data = {"mode": 1,
            "remark": "",
            "goodsType": "MEDICINE",
            "detail": [{"medicineId": 421,
                        "medicineType": "EQUIPMENT",
                        "unitId": 997,
                        "stock": "100"},
                        {"medicineId": 420,
                         "medicineType": "PATENT",
                         "unitId": 995,
                         "stock": "100"},
                        {"medicineId": 419,
                         "medicineType": "HERB",
                         "unitId": 993,
                         "stock": "100"}
                       ]}
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def create_medicine_charge():
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineTakestock/takestockCreate"
    data = {
            "mode": 2,
            "remark": "",
            "goodsType": "MEDICINE",
            "detail": [{"medicineId": 421,
                        "medicineType": "EQUIPMENT",
                        "unitId": 997,
                        "price": "100"},
                       {"medicineId": 420,
                        "medicineType": "PATENT",
                        "unitId": 995,
                        "price": "100"},
                       {"medicineId": 419,
                        "medicineType": "HERB",
                        "unitId": 993,
                        "price": "100"}]
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def create_mall_commodity_takestock():
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineTakestock/takestockCreate"
    data = {
            "mode": 1,
            "remark": "",
            "goodsType": "MALL",
            "mallDetail": [{"sid": 280, "stock": "100"}]
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def create_mall_commodity_charge():
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineTakestock/takestockCreate"
    data = {
            "mode": 2,
            "remark": "",
            "goodsType": "MALL",
            "mallDetail": [{"sid": 280,
                            "price": "100"}]
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()
