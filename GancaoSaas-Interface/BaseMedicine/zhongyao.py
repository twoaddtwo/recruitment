import unittest
from BaseMedicine import zhongyao_d
import random


class Zhongyao(unittest.TestCase):

    random_num = random.randint(0, 9999)
    zhongyao_title = "藿香正气水" + str(random_num)
    chengyao_titile = "成药一号" + str(random_num)
    qixie_title = "器械" + str(random_num)
    medicine_item_title = "诊疗项目" + str(random_num)
    medicine_supplier_title = "供应商" + str(random_num)
    commodity_title = "商城产品" + str(random_num)

    def test_create_zhongyao(self):
        result = zhongyao_d.create_zhongyao(self.zhongyao_title, "HERB")
        self.assertEqual("药材新增成功", result['message'])
        result, results = zhongyao_d.query_zhongyao(self.zhongyao_title)
        zhongyao_id = results[0][0]
        result = zhongyao_d.update_zhongyao(zhongyao_id, self.zhongyao_title, "HERB")
        self.assertEqual("药材修改成功", result['message'])
        result = zhongyao_d.stop_zhongyao(zhongyao_id, 0, "HERB")
        self.assertEqual("批量修改成功", result['message'])
        result = zhongyao_d.stop_zhongyao(zhongyao_id, 1, "HERB")
        self.assertEqual("批量修改成功", result['message'])
        result = zhongyao_d.get_zhongyao_list("HERB")
        self.assertEqual("药材库存列表获取成功", result['message'])
        result = zhongyao_d.inport_zhongyao("HERB")
        self.assertEqual("请求成功", result['message'])

    def test_create_chengyao(self):
        result = zhongyao_d.create_zhongyao(self.chengyao_titile, "PATENT")
        self.assertEqual("药材新增成功", result['message'])
        result, results = zhongyao_d.query_zhongyao(self.chengyao_titile)
        chengyao_id = results[0][0]
        result = zhongyao_d.update_zhongyao(chengyao_id, self.chengyao_titile, "PATENT")
        self.assertEqual("药材修改成功", result['message'])
        result = zhongyao_d.stop_zhongyao(chengyao_id, 0, "PATENT")
        self.assertEqual("批量修改成功", result['message'])
        result = zhongyao_d.stop_zhongyao(chengyao_id, 1, "PATENT")
        self.assertEqual("批量修改成功", result['message'])
        result = zhongyao_d.get_zhongyao_list("PATENT")
        self.assertEqual("药材库存列表获取成功", result['message'])
        result = zhongyao_d.inport_zhongyao("PATENT")
        self.assertEqual("请求成功", result['message'])

    def test_create_qixie(self):
        result = zhongyao_d.create_zhongyao(self.qixie_title, "EQUIPMENT")
        self.assertEqual("药材新增成功", result['message'])
        result, results = zhongyao_d.query_zhongyao(self.qixie_title)
        qixie_id = results[0][0]
        result = zhongyao_d.update_zhongyao(qixie_id, self.qixie_title, "EQUIPMENT")
        self.assertEqual("药材修改成功", result['message'])
        result = zhongyao_d.stop_zhongyao(qixie_id, 0, "EQUIPMENT")
        self.assertEqual("批量修改成功", result['message'])
        result = zhongyao_d.stop_zhongyao(qixie_id, 1, "EQUIPMENT")
        self.assertEqual("批量修改成功", result['message'])
        result = zhongyao_d.get_zhongyao_list("EQUIPMENT")
        self.assertEqual("药材库存列表获取成功", result['message'])
        result = zhongyao_d.inport_zhongyao("EQUIPMENT")
        self.assertEqual("请求成功", result['message'])

    def test_create_medicine_item(self):
        result = zhongyao_d.create_medicine_item(self.medicine_item_title)
        self.assertEqual("诊疗项目添加成功", result['message'])
        medicine_item_id = result['data']
        result = zhongyao_d.update_medicine_item(medicine_item_id, self.medicine_item_title)
        self.assertEqual("药材修改成功", result['message'])
        result = zhongyao_d.stop_medicine_item(medicine_item_id, 0)
        self.assertEqual("批量修改成功", result['message'])
        result = zhongyao_d.stop_medicine_item(medicine_item_id, 1)
        self.assertEqual("批量修改成功", result['message'])
        result = zhongyao_d.inport_medicine_item()
        self.assertEqual("请求成功", result['message'])

    def test_create_medicine_supplier(self):
        result = zhongyao_d.create_medicine_supplier(self.medicine_supplier_title)
        self.assertEqual("供应商新增成功", result['message'])
        medicine_supplier_id = result['data']
        result = zhongyao_d.update_medicine_supplier(medicine_supplier_id, self.medicine_supplier_title)
        self.assertEqual("供应商修改成功", result['message'])
        result = zhongyao_d.stop_medicine_supplier(medicine_supplier_id, 0)
        self.assertEqual("批量修改成功", result['message'])
        result = zhongyao_d.stop_medicine_supplier(medicine_supplier_id, 1)
        self.assertEqual("批量修改成功", result['message'])

    def test_create_mall_commodity(self):
        result = zhongyao_d.create_mall_commodity(self.commodity_title)
        self.assertEqual("商城商品新增成功", result['message'])
        commodity_id = result['data']
        result = zhongyao_d.update_mall_commodity(self.commodity_title, commodity_id)
        self.assertEqual("修改商品成功", result['message'])
        result = zhongyao_d.stop_mall_commodity(commodity_id, 0)
        self.assertEqual("批量修改成功", result['message'])
        result = zhongyao_d.stop_mall_commodity(commodity_id, 1)
        self.assertEqual("批量修改成功", result['message'])






