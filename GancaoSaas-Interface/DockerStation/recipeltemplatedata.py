import requests
import json
from Common import common

def create_recipeltemplate_cloud(templatename, type):
    url = "https://test.igancao.cn:8000/gateway/treatment/recipelTemplate/addRecipelTemplate"
    data = {
            "isGancao": 1,
            "medicineType": "",
            "content": "[{\"i\":286,\"t\":\"大枣\",\"l\":0,\"b\":\"\",\"k\":100,\"u\":\"克\",\"p\":0.051},{\"i\":281,\"t\":\"红花\",\"l\":0,\"b\":\"\",\"k\":100,\"u\":\"克\",\"p\":0.34599999},{\"i\":879,\"t\":\"蜜枇杷叶\",\"l\":0,\"b\":\"\",\"k\":100,\"u\":\"克\",\"p\":0.03},{\"i\":651,\"t\":\"通天草\",\"l\":0,\"b\":\"\",\"k\":100,\"u\":\"克\",\"p\":0.06},{\"i\":270,\"t\":\"合欢皮\",\"l\":0,\"b\":\"\",\"k\":100,\"u\":\"克\",\"p\":0.031}]",
            "templateName": "云药方" + templatename,
            "templateType": type
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def create_recipeltemplate_zhongyao(templatename, type):
    url = "https://test.igancao.cn:8000/gateway/treatment/recipelTemplate/addRecipelTemplate"
    data = {
            "isGancao": 0,
            "medicineType": "HERB",
            "content": "[{\"i\":419,\"b\":\"\",\"k\":1,\"n\":993,\"u\":\"克\"},{\"i\":416,\"b\":\"\",\"k\":1,\"n\":987,\"u\":\"克\"}]",
            "templateName": "中药" + templatename,
            "templateType": type
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def create_recipeltemplate_chengyao(templatename, type):
    url = "https://test.igancao.cn:8000/gateway/treatment/recipelTemplate/addRecipelTemplate"
    data = {
            "isGancao": 0,
            "medicineType": "PATENT",
            "content": "[{\"i\":420,\"b\":\"\",\"k\":100,\"n\":995,\"d\":100,\"a\":\"呃呃大的点点滴滴\"},{\"i\":129,\"b\":\"\",\"k\":100,\"n\":282,\"d\":100,\"a\":\"用药方式口服\"}]",
            "templateName": "成药模版" + templatename,
            "templateType": type
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()

def create_recipeltemplate_qixie(templatename, type):
    url = "https://test.igancao.cn:8000/gateway/treatment/recipelTemplate/addRecipelTemplate"
    data = {
            "isGancao": 0,
            "medicineType": "EQUIPMENT",
            "content": "[{\"i\":421,\"b\":\"\",\"k\":100,\"n\":997,\"a\":\"\"},{\"i\":391,\"b\":\"\",\"k\":100,\"n\":944,\"a\":\"\"}]",
            "templateName": "器械模版" + templatename,
            "templateType": type
            }
    r = requests.post(url, headers=common.headers, data= json.dumps(data), verify=False)
    return r.json()


def create_recipeltemplate_item(templatename, type):
    url = "https://test.igancao.cn:8000/gateway/treatment/recipelTemplate/addRecipelTemplate"
    data = {
            "isGancao": 0,
            "medicineType": "PROJECT",
            "content": "[{\"i\":199,\"b\":\"\",\"k\":100,\"u\":\"大箱\"},{\"i\":198,\"b\":\"\",\"k\":100,\"u\":\"大箱\"}]",
            "templateName": "诊疗项目" + templatename,
            "templateType": type
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def update_recipeltemplate_cloud(templatename, id ,type):
    url = " https://test.igancao.cn:8000/gateway/treatment/recipelTemplate/updateRecipelTemplate"
    data = {
            "isGancao": 1,
            "medicineType": "CLOUD",
            "content": "[{\"i\":286,\"t\":\"大枣\",\"l\":0,\"b\":\"\",\"k\":100,\"u\":\"克\",\"p\":0.051},{\"i\":281,\"t\":\"红花\",\"l\":0,\"b\":\"\",\"k\":100,\"u\":\"克\",\"p\":0.34599999},{\"i\":879,\"t\":\"蜜枇杷叶\",\"l\":0,\"b\":\"\",\"k\":100,\"u\":\"克\",\"p\":0.03},{\"i\":651,\"t\":\"通天草\",\"l\":0,\"b\":\"\",\"k\":100,\"u\":\"克\",\"p\":0.06},{\"i\":270,\"t\":\"合欢皮\",\"l\":0,\"b\":\"\",\"k\":100,\"u\":\"克\",\"p\":0.031}]",
            "templateName": "修改" + templatename,
            "templateType": type,
            "recipelTemplateId": id
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def update_recipeltemplate_zhongyao(templatename, id, type):
    url = "https://test.igancao.cn:8000/gateway/treatment/recipelTemplate/updateRecipelTemplate"
    data = {
            "isGancao": 0,
            "medicineType": "HERB",
            "content": "[{\"i\":419,\"b\":\"\",\"k\":1,\"n\":993,\"u\":\"克\"},{\"i\":416,\"b\":\"\",\"k\":1,\"n\":987,\"u\":\"克\"}]",
            "templateName": "修改" + templatename,
            "templateType": type,
            "recipelTemplateId": id
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def update_recipeltemplate_chengyao(templatename, id, type):
    url = "https://test.igancao.cn:8000/gateway/treatment/recipelTemplate/updateRecipelTemplate"
    data = {
            "isGancao": 0,
            "medicineType": "PATENT",
            "content": "[{\"i\":420,\"b\":\"\",\"k\":100,\"n\":995,\"u\":\"克\",\"d\":100,\"a\":\"呃呃大的点点滴滴\"},{\"i\":129,\"b\":\"\",\"k\":100,\"n\":282,\"u\":\"克\",\"d\":100,\"a\":\"用药方式口服\"}]",
            "templateName": "修改" + templatename,
            "templateType": type,
            "recipelTemplateId": id
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def update_recipeltemplate_qixie(templatename, id, type):
    url = "https://test.igancao.cn:8000/gateway/treatment/recipelTemplate/updateRecipelTemplate"
    data = {
            "isGancao": 0,
            "medicineType": "EQUIPMENT",
            "content": "[{\"i\":421,\"b\":\"\",\"k\":100,\"n\":997,\"u\":\"克\",\"a\":\"\"},{\"i\":391,\"b\":\"\",\"k\":100,\"n\":944,\"u\":\"克\",\"a\":\"\"}]",
            "templateName": "修改" + templatename,
            "templateType": type,
            "recipelTemplateId": id
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def update_recipeltemplate_item(templatename, id, type):
    url = "https://test.igancao.cn:8000/gateway/treatment/recipelTemplate/updateRecipelTemplate"
    data = {
            "isGancao": 0,
            "medicineType": "PROJECT",
            "content": "[{\"i\":199,\"b\":\"\",\"k\":100,\"u\":\"大箱\"},{\"i\":198,\"b\":\"\",\"k\":100,\"u\":\"大箱\"}]",
            "templateName": "修改" + templatename,
            "templateType": type,
            "recipelTemplateId": id
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()



