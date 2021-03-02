import unittest
from BaseMedicine import zhongyao_d
from DB import DB


class Zhongyao(unittest.TestCase):

    def test_create_zhongyao(self):
        zhongyao_d.create_zhongyao(zhongyao_d.create_zhongyao_url, zhongyao_d.create_zhongyao_headers, zhongyao_d.create_zhongyao_data)
        DB.exe_sql(zhongyao_d.create_zhongyao_sql)

