import unittest
from BaseMedicine import zhongyao_d
import random


class Zhongyao(unittest.TestCase):

    random_num = random.randint(0, 9999)
    zhongyao_title = "藿香正气水" + str(random_num)

    def test_create_zhongyao(self):
        zhongyao_d.create_zhongyao(self.zhongyao_title)
        zhongyao_d.query_zhongyao(self.zhongyao_title)

