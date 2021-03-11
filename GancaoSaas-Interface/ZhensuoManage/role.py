from ZhensuoManage import roledata
import unittest


class Role(unittest.TestCase):

    def test_create_role(self):
        result = roledata.create_role()
        self.assertEqual("角色新增成功", result['message'])
        id = result['data']
        result = roledata.update_role(id)
        self.assertEqual("角色修改成功", result['message'])
        result = roledata.delete_role(id)
        self.assertEqual("角色删除成功", result['message'])

