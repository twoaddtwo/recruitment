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
        employeedata.create_employee(phone, authcode)
        login.send_authcode(phone)
        login.authcode_login(phone, authcode)

