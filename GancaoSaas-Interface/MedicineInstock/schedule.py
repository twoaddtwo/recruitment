import unittest
from MedicineInstock import scheduledata
import time


class Schedule(unittest.TestCase):

    now = time.strftime("%Y-%m-%d", time.localtime())


    def test_create_schedule(self):
        result = scheduledata.create_schedule(self.now)
        self.assertEqual("排班创建成功", result['message'])
        result, results = scheduledata.query_schedule_id(self.now)
        schedule_id = results[0][0]
        result = scheduledata.update_schedule(schedule_id, self.now)
        self.assertEqual("排班修改成功", result['message'])
        result = scheduledata.cancel_schedule(schedule_id)
        self.assertEqual("取消排班成功", result['message'])
