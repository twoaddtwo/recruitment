import instockdata
import unittest


class Instock(unittest.TestCase):

    def test_create_medicine_instock(self):
        result = instockdata.create_medicine_instock()
        self.assertEqual("药材入库单新增成功", result['message'])
        result = instockdata.create_medicine_outstock()
        self.assertEqual("药出库单新增成功", result['message'])
        result = instockdata.create_mall_commodity_instock()
        self.assertEqual("药材入库单新增成功", result['message'])
        result = instockdata.create_mall_commodity_outstock()
        self.assertEqual("药出库单新增成功", result['message'])

