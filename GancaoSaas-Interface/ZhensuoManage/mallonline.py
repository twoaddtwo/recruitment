from ZhensuoManage import mallonlinedata
import unittest


class Mallonline(unittest.TestCase):
    def test_save_mallbanner(self):
        result = mallonlinedata.save_mallbanner()
        self.assertEqual("保存商城banner成功!", result['message'])

