import random
from Common import common
import requests
import json

random_num = random.randint(0, 9999)
zhongyao_title = "藿香正气水" + str(random_num)

create_zhongyao_url = "https://test.igancao.cn:8000/gateway/pharmacy/medicine/createHerb"
create_zhongyao_headers = common.headers
create_zhongyao_data = {
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

create_zhongyao_sql = "select * from gd_default.pharmacy_medicine_herb where title = '%s'" % zhongyao_title


def create_zhongyao(url, headers, data):
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(r.json())