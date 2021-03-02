from Login.login import Login
import random

login = Login()
login_url = "https://test.igancao.cn:8000/gateway/base/employee/login"
login_headers = {"content-type": "application/json", "access_shop": "199", "access_version": "development"}
login_data = {"type": "2", "passport": "xiaowen", "password": "123123qaz"}
token = login.login(login_url, login_headers, login_data)


headers = {"content-type": "application/json", "access_shop": "199", "access_version": "development", "access_token": token}

random_num = random.randint(0, 9999)
zhongyao_title = "藿香正气水" + str(random_num)
create_zhongyao_url = "https://test.igancao.cn:8000/gateway/pharmacy/medicine/createHerb"
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
