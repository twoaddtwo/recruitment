import login
import requests
import json


def create_self_zhongyao():
    url = "https://test.igancao.cn:8000/gateway/treatment/recipel/createRecipel"
    headers = login.headers
    data = {
	"amount": 7,
	"content": "[{\"i\":3742,\"b\":\"\",\"k\":1,\"r\":0,\"n\":6202,\"u\":\"克\"}]",
	"docAdvice": 1,
	"docAdviceName": "",
	"frequency": "50ml包，一天2次",
	"isDecoction": 1,
	"medicalAdvice": "",
	"medicineType": "HERB",
	"modeId": 147,
	"sort": 1,
	"prescriptionId": 2785,
	"remark": "",
	"isDocking": 0,
	"dockingId": -1,
	"from": 0
}
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(r.json())
    return r.json()['data']

def create_self_xiyao():
    url = "https://test.igancao.cn:8000/gateway/treatment/recipel/createRecipel"
    headers = login.headers
    data = {
	"content": "[{\"i\":3162,\"b\":\"\",\"k\":1,\"n\":5391,\"d\":1,\"a\":\"随便\"}]",
	"medicalAdvice": "",
	"medicineType": "PATENT",
	"sort": 2,
	"prescriptionId": 2785,
	"remark": "",
	"isDocking": 0,
	"dockingId": -1,
	"from": 0
}
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(r.json())
    return r.json()['data']

def create_self_yiliaoqixie():
    url = "https://test.igancao.cn:8000/gateway/treatment/recipel/createRecipel"
    headers = login.headers
    data = {
	"content": "[{\"i\":3163,\"b\":\"\",\"k\":1,\"n\":5392,\"a\":\"\"}]",
	"medicalAdvice": "",
	"medicineType": "EQUIPMENT",
	"sort": 3,
	"prescriptionId": 2785,
	"remark": "",
	"isDocking": 0,
	"dockingId": -1,
	"from": 0
}
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(r.json())
    return r.json()['data']

def create_self_zhenliaoxiangmu():
    url = "https://test.igancao.cn:8000/gateway/treatment/recipel/createRecipel"
    headers = login.headers
    data = {
	"content": "[{\"i\":218,\"b\":\"\",\"k\":1,\"u\":\"次\"}]",
	"medicalAdvice": "",
	"medicineType": "PROJECT",
	"sort": 4,
	"prescriptionId": 2785,
	"remark": "",
	"isDocking": 0,
	"dockingId": -1,
	"from": 0
}
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(r.json())
    return r.json()['data']

def create_self_shangchengchanpin():
    url = "https://test.igancao.cn:8000/gateway/treatment/recipel/createRecipel"
    headers = login.headers
    data = {
	"content": "[{\"i\":362,\"b\":\"\",\"k\":1}]",
	"medicalAdvice": "",
	"medicineType": "MALL",
	"sort": 5,
	"prescriptionId": 2785,
	"remark": "",
	"isDocking": 0,
	"dockingId": -1,
	"from": 0
}
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(r.json())
    return r.json()['data']

