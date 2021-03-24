import json
import requests
from Common import common


def create_medicine_instock():
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineInstock/intoInstock"
    data = {"payType": 1,
            "remark": "",
            "supplierId": "",
            "mode": 2,
            "timeline": "2021-03-24",
            "goodsType": "MEDICINE",
            "detail": [{"medicineId": 421,
                       "medicineType": "EQUIPMENT",
                       "unitId": 997,
                       "unitAmount": "1",
                       "unitPrice": 1,
                       "money": 1,
                       "batch": ""},
                      {"medicineId": 420,
                       "medicineType": "PATENT",
                       "unitId": 995,
                       "unitAmount": "1",
                       "unitPrice": 1,
                       "money": 1,
                       "batch": ""},
                      {"medicineId": 419,
                       "medicineType": "HERB",
                       "unitId": 993,
                       "unitAmount": "1",
                       "unitPrice": 1,
                       "money": 1,
                       "batch": ""}]
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def create_medicine_outstock():
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineInstock/outInstock"
    data = {
            "payType": 1,
            "remark": "",
            "supplierId": "",
            "mode": 2,
            "timeline": "2021-03-24",
            "goodsType": "MEDICINE",
            "detail": [{"medicineId": 421,
                        "medicineType": "EQUIPMENT",
                        "unitId": 997,
                        "unitAmount": "1",
                        "unitPrice": 1,
                        "money": 1,
                        "batch": ""},
                       {"medicineId": 420,
                        "medicineType": "PATENT",
                        "unitId": 995,
                        "unitAmount": "1",
                        "unitPrice": 1,
                        "money": 1,
                        "batch": ""},
                       {"medicineId": 419,
                        "medicineType": "HERB",
                        "unitId": 993,
                        "unitAmount": "1",
                        "unitPrice": 1,
                        "money": 1,
                        "batch": ""}]
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def create_mall_commodity_instock():
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineInstock/intoInstock"
    data = {
            "payType": 1,
            "remark": "",
            "supplierId": "",
            "mode": 2,
            "timeline": "2021-03-24",
            "goodsType": "MALL",
            "mallDetail": [{"sid": 280, "amount": "1", "price": 1, "money": 1, "batchNumber": ""}]
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def create_mall_commodity_outstock():
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineInstock/outInstock"
    data = {
            "payType": 1,
            "remark": "",
            "supplierId": "",
            "mode": 2,
            "timeline": "2021-03-24",
            "goodsType": "MALL",
            "mallDetail": [{"sid": 280,
                            "amount": "1",
                            "price": 1,
                            "money": 1,
                            "batchNumber": ""}]
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()




