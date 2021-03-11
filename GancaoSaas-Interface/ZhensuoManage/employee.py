import unittest
from ZhensuoManage import employeedata
from Login import login
import random

random_num = random.randint(18800000000, 18899999999)
phone = str(random_num)
authcode = phone[7:11]
print(phone)
print(authcode)


class Employee(unittest.TestCase):

    def test_create_employee(self):
        result, id = employeedata.create_employee(phone, authcode)
        self.assertEqual("用户新增成功", result['message'])
        result = login.send_authcode(phone)
        self.assertEqual("验证码发送成功!", result['message'])
        result = login.authcode_login(phone, authcode)
        self.assertEqual("登录成功", result['message'])
        result = employeedata.update_employee(phone, authcode, id)
        self.assertEqual("用户修改成功", result['message'])
        result = employeedata.query_employee(id)
        self.assertEqual("查询到数据", result)
        result = employeedata.disable_employee(id, -1)
        self.assertEqual("操作成功", result['message'])
        employeedata.disable_employee(id, 1)
        self.assertEqual("操作成功", result['message'])
        result = employeedata.del_employee(id)
        self.assertEqual("删除成功", result)
        result = employeedata.query_employee(id)
        self.assertEqual("没有查询到数据", result)



