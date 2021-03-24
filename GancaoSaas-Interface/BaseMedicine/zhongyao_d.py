from Common import common
import requests
import json
from DB import DB


def create_zhongyao(title, medicinetype):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicine/createHerb"
    headers = common.headers
    data = {
            "mutiChecked": "false",
            "times": "1",
            "alias": [],
            "unit": [],
            "retailUnit": "克",
            "retailPrice": "10",
            "code": "",
            "format": "",
            "pharmaTitle": "",
            "remark": "",
            "title": title,
            "type": "",
            "standardCode": "",
            "nmpn": "",
            "py": "HXZQS",
            "takeMethod": "",
            "medicineType": medicinetype
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def query_zhongyao(zhongyao_title):
    query_zhongyao_sql = "select id from gd_default.pharmacy_medicine_herb where title = '%s'" % zhongyao_title
    result, results = DB.exe_sql(query_zhongyao_sql)
    return result, results


def update_zhongyao(id, title, medicinetype):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicine/updateHerb"
    headers = common.headers
    data = {
            "mutiChecked": "false",
            "times": 1,
            "alias": [],
            "unit": [],
            "retailUnit": "克",
            "retailPrice": "10",
            "code": "",
            "format": "",
            "pharmaTitle": "",
            "remark": "",
            "title": title + "修改",
            "type": "",
            "standardCode": "",
            "nmpn": "",
            "py": "HXZQSXG",
            "takeMethod": "",
            "id": id,
            "medicineType": medicinetype,
            "isSale": 1,
            "aliasString": "",
            "total": 0,
            "totalAvailable": 0
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def stop_zhongyao(id, enable, medicinetype):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicine/batchSale"
    headers = common.headers
    data = {
            "ids": id,
            "isSale": enable,
            "medicineType": medicinetype
            }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()



def get_zhongyao_list(medicinetype):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicine/getList"
    headers = common.headers
    data = {
            "isSale": "1",
            "kw": "",
            "nmpn": "",
            "standardCode": "",
            "medicineType": medicinetype,
            "pageNum": 1,
            "pageSize": 10
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def inport_zhongyao(medicinetype):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicine/inportData"
    headers = {"access_shop": "199", "access_version": "development",
               "access_token": common.token}
    data = {"medicineType": medicinetype}
    files = {'file': ('药材导入.xls', open('/Users/zhaoxinyu/Desktop/GancaoSaas-Interface/BaseMedicine/药材导入.xls', 'rb'))}
    r = requests.post(url, headers=headers, data=data, files=files, verify=False)
    return r.json()


def create_medicine_item(medicine_item_title):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineTreatmentItems/create"
    data = {
            "mutiChecked": "false",
            "times": 1,
            "alias": [],
            "unit": [],
            "retailUnit": "大箱",
            "retailPrice": "2",
            "code": "",
            "format": "",
            "pharmaTitle": "",
            "remark": "",
            "title": medicine_item_title,
            "type": "",
            "standardCode": "",
            "nmpn": "",
            "py": "",
            "takeMethod": "",
            "medicineType": "TREATITEM"
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def update_medicine_item(id, title):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineTreatmentItems/update"
    data = {
            "mutiChecked": "false",
            "times": 1,
            "alias": [],
            "unit": [],
            "retailUnit": "大箱",
            "retailPrice": "2",
            "code": "",
            "format": "",
            "pharmaTitle": "",
            "remark": "",
            "title": title + "修改",
            "type": "",
            "standardCode": "",
            "nmpn": "",
            "py": "",
            "takeMethod": "",
            "id": id,
            "isSale": 1,
            "medicineType": "TREATITEM"
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def stop_medicine_item(id, enbale):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineTreatmentItems/batchSale"
    data = {
            "ids": id,
            "isSale": enbale,
            "medicineType": "TREATITEM"
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def inport_medicine_item():
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineTreatmentItems/inportData"
    headers = {"access_shop": "199", "access_version": "development",
               "access_token": common.token}
    files = {'file': ('诊疗项目导入.xls', open('/Users/zhaoxinyu/Desktop/GancaoSaas-Interface/BaseMedicine/诊疗项目导入.xls', 'rb'))}
    r = requests.post(url, headers=headers, files=files, verify=False)
    return r.json()


def create_medicine_supplier(suppliername):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineSupplier/create"
    data = {
            "id": "",
            "supplierCode": "",
            "supplierName": suppliername,
            "contactsName": "",
            "contactsPhone": 13342236666,
            "supplierProvince": 1,
            "supplierCity": 3587,
            "supplierDistrict": 36,
            "supplierAddress": "11111",
            "remark": "444444"
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def update_medicine_supplier(id, suppliername):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineSupplier/update"
    data = {
            "id": id,
            "supplierCode": suppliername,
            "supplierName": suppliername + "修改",
            "contactsName": "",
            "contactsPhone": "13342236666",
            "supplierProvince": 1,
            "supplierCity": 3587,
            "supplierDistrict": 36,
            "supplierAddress": "11111",
            "remark": "444444"
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def stop_medicine_supplier(id, enable):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/medicineSupplier/batchEnabled"
    data = {
            "ids": id,
            "isEnable": enable
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def create_mall_commodity(commodity_title):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/mallCommodity/createCommodity"
    data = {
            "title": commodity_title,
            "pharmaTitle": "",
            "type": "",
            "commoditySubs": [{"code": commodity_title, "title": commodity_title, "unit": "克", "money": 1, "isSale": 1}],
            "photo": "",
            "detail": "",
            "remark": ""
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def update_mall_commodity(commodity_title, commodity_id):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/mallCommodity/updateCommodity"
    data = {
            "id": commodity_id,
            "title": commodity_title + "修改",
            "pharmaTitle": "",
            "commoditySubs": [{"code": commodity_title + "修改", "title": "修改" + commodity_title, "unit": "克", "money": 20, "isSale": 1, "id": 332}],
            "photo": "",
            "detail": "",
            "remark": ""
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def stop_mall_commodity(commodity_id, enable):
    url = "https://test.igancao.cn:8000/gateway/pharmacy/mallCommodity/batchSale"
    data = {
            "ids": commodity_id,
            "isSale": enable}
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()




