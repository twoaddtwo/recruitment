import json
import requests
from Common import common
from DB import DB

def create_patient(phone):
    url = "https://test.igancao.cn:8000/gateway/treatment/treatmentDoctor/addMyPatient"
    data = {
            "deliveryAddressList": [],
            "patientInfo": {
                            "address": "",
                            "age": 10,
                            "allergy": "",
                            "birthday": "",
                            "cardNumber": "",
                            "cardType": "",
                            "city": "",
                            "emergencyContact": "",
                            "emergencyContactPhone": "",
                            "height": "",
                            "name": "11",
                            "past": "",
                            "phone": phone,
                            "province": "",
                            "region": "",
                            "sex": 1,
                            "weight": ""
                            }
            }
    r = requests.post(url, headers=common.headers, data=json.dumps(data), verify=False)
    return r.json()


def query_patient_number(phone):
    query_patient_num_sql = "select medical_number, patient_id from gd_default.treatment_doctor_patient where phone = '%s'" % phone
    result, results = DB.exe_sql(query_patient_num_sql)
    return result, results


