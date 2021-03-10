from Common import common
import requests
import json
from DB import DB


def create_zhongyao(zhongyao_title):

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
        "title": zhongyao_title,
        "type": "",
        "standardCode": "",
        "nmpn": "",
        "py": "HXZQS",
        "takeMethod": "",
        "medicineType": "HERB"
    }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(r.json())


def query_zhongyao(zhongyao_title):
    query_zhongyao_sql = "select * from gd_default.pharmacy_medicine_herb where title = '%s'" % zhongyao_title
    DB.exe_sql(query_zhongyao_sql)