import unittest
import sys
import os
import time
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print(curPath)
print(rootPath)

from BaseMedicine.zhongyao import Zhongyao
from ZhensuoManage.employee import Employee
from ZhensuoManage.config import Config
from ZhensuoManage.desk import Desk
from ZhensuoManage.role import Role
from DockerStation.patient import Patient
from DockerStation.recipeltemplate import Recipeltemplate
from MedicineInstock.instock import Instock
from MedicineInstock.schedule import Schedule
from MedicineInstock.takestock import Takestock
from VipCard.viplist import Vipcard
from BeautifulReport import BeautifulReport


def mysuit():
    suite = unittest.TestSuite()
    suite.addTest(Zhongyao("test_create_zhongyao"))
    suite.addTest(Zhongyao("test_create_chengyao"))
    suite.addTest(Zhongyao("test_create_qixie"))
    suite.addTest(Zhongyao("test_create_medicine_item"))
    suite.addTest(Zhongyao("test_create_medicine_supplier"))
    suite.addTest(Zhongyao("test_create_mall_commodity"))

    suite.addTest(Employee("test_create_employee"))

    suite.addTest(Config("test_create_treatmentmode"))
    suite.addTest(Config("test_create_class"))
    suite.addTest(Config("test_config_appointment"))
    suite.addTest(Config("test_config_cloud_pharmacy"))
    suite.addTest(Config("test_sysinfo"))
    suite.addTest(Config("test_membercard"))
    suite.addTest(Config("test_dock"))

    suite.addTest(Desk("test_create_desk"))

    suite.addTest(Role("test_create_role"))
    suite.addTest(Patient("test_create_mypatient"))
    suite.addTest(Recipeltemplate("test_create_recipeltemplate"))
    suite.addTest(Instock("test_create_medicine_instock"))
    suite.addTest(Schedule("test_create_schedule"))
    suite.addTest(Takestock("test_create_medicine_takestock"))
    suite.addTest(Vipcard("test_create_vipcard"))




    return suite


if __name__ == '__main__':
    # runner = unittest.TextTestRunner(verbosity=2).run(mysuit())
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = now + '.html'
    result = BeautifulReport(mysuit())
    result.report(filename=filename, description='测试报告', log_path='.')
