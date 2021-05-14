import unittest
from MedicineInstock import takestockdata


class Takestock(unittest.TestCase):


    def test_create_medicine_takestock(self):
        result = takestockdata.create_medicine_takestock()
        self.assertEqual("盘库单新增成功", result['message'])
        result = takestockdata.create_medicine_charge()
        self.assertEqual("盘库单新增成功", result['message'])
        result = takestockdata.create_mall_commodity_takestock()
        self.assertEqual("盘库单新增成功", result['message'])
        result = takestockdata.create_mall_commodity_charge()
        self.assertEqual("盘库单新增成功", result['message'])
