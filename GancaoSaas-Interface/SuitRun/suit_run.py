import unittest
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print(curPath)
print(rootPath)

from BaseMedicine.zhongyao import Zhongyao
from ZhensuoManage.employee import Employee
from BeautifulReport import BeautifulReport


def mysuit():
    suite = unittest.TestSuite()
    # suite.addTest(Zhongyao("test_create_zhongyao"))
    suite.addTest(Employee("test_create_employee"))


    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2).run(mysuit())
    # now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # filename = now + '.html'
    # result = BeautifulReport(mysuit())
    # result.report(filename=filename, description='测试报告', log_path='.')
