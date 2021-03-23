from ZhensuoManage import deskdata
import unittest
import random


class Desk(unittest.TestCase):
    code = random.randint(11111, 19999)

    def test_create_desk(self):
        result = deskdata.create_desk(self.code)
        self.assertEqual("科室新增成功", result['message'])
        result, results = deskdata.query_deskid(self.code)
        print(results[0][0])
        deskid = results[0][0]
        result = deskdata.update_desk(self.code, deskid)
        self.assertEqual("科室修改成功", result['message'])
        result = deskdata.disable_desk(deskid, -1)
        self.assertEqual("操作成功", result['message'])
        result = deskdata.disable_desk(deskid, 1)
        self.assertEqual("操作成功", result['message'])

        result = deskdata.create_room(self.code, deskid)
        self.assertEqual("诊室新增成功", result['message'])
        result, results = deskdata.query_roomid(self.code)
        roomid = results[0][0]
        result = deskdata.update_room(self.code, roomid)
        self.assertEqual("诊室修改成功", result['message'])
        result = deskdata.disable_room(roomid, -1)
        self.assertEqual("操作成功", result['message'])
        result = deskdata.disable_room(roomid, 1)
        self.assertEqual("操作成功", result['message'])
