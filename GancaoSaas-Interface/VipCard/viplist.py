import unittest
from VipCard import viplistdata
from DockerStation import patientdata
import random


class Vipcard(unittest.TestCase):
    random_num = random.randint(18800000000, 18899999999)
    phone = str(random_num)

    def test_create_vipcard(self):
        result = viplistdata.get_vipcard_num()
        self.assertEqual("卡号生成成功!", result['message'])
        cardnum = result['data']
        result = patientdata.create_patient(self.phone)
        self.assertEqual("患者新增成功", result['message'])
        result, results = patientdata.query_patient_number(self.phone)
        patientnum = results[0][0]
        patientid = results[0][1]
        result = viplistdata.create_vipcard(cardnum, self.phone, patientnum, patientid)
        self.assertEqual("开卡成功!", result['message'])
        vipcard_id = result['data']['id']
        result = viplistdata.create_vipcard_tocharge(vipcard_id)
        self.assertEqual("去充值请求成功!", result['message'])
        result = viplistdata.create_vipcard_refund(vipcard_id)
        self.assertEqual("退款成功!", result['message'])




