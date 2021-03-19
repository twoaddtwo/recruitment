from ZhensuoManage import configdata
import unittest
import random

random_num = random.randint(1111, 9999)


title = "剂型名称测试"
membercardtitle = "小龙金卡" + str(random_num)

class Config(unittest.TestCase):


    def test_create_treatmentmode(self):
        configdata.create_treatmentmode(title)
        result, results = configdata.query_treatmentmode_id(title)
        treatmentmode_id = results[0][0]
        result = configdata.update_treatmentmode(treatmentmode_id)
        self.assertEqual("剂型&用药频次更新成功", result['message'])
        result = configdata.create_medication_frequency(treatmentmode_id)
        self.assertEqual("剂型&用药频次更新成功", result['message'])
        result = configdata.update_medication_frequency(treatmentmode_id)
        self.assertEqual("剂型&用药频次更新成功", result['message'])

    def test_create_class(self):
        result = configdata.create_class()
        self.assertEqual("创建班次成功!", result['message'])
        class_id = result['data']
        result = configdata.update_class(class_id)
        self.assertEqual("修改班次成功!", result['message'])
        result = configdata.delete_class(class_id)
        self.assertEqual("删除班次成功!", result['message'])


    def test_config_appointment(self):
        result = configdata.config_appointment(30)
        self.assertEqual("设置通用配置成功!", result['message'])


    def test_config_cloud_pharmacy(self):
        result = configdata.get_cloud_pharmacy_configlist()
        self.assertEqual("云药房配置列表获取成功", result['message'])
        result = configdata.update_cloud_pharmacy_config(result['data'])
        self.assertEqual("云药房自定义收益比例配置修改成功", result['message'])


    def test_sysinfo(self):
        result = configdata.update_sysinfo()
        self.assertEqual("诊所信息修改成功", result['message'])


    def test_membercard(self):
        result = configdata.create_membercard_type(membercardtitle)
        self.assertEqual("创建会员类型成功!", result['message'])
        result, results = configdata.query_membercard_id(membercardtitle)
        membercard_id = results[0][0]
        result = configdata.update_membercard_type(membercard_id, membercardtitle)
        self.assertEqual("修改会员类型成功!", result['message'])
        result = configdata.stop_membercard_type(membercard_id)
        self.assertEqual("修改会员类型状态成功!", result['message'])
        result = configdata.config_membercard()
        self.assertEqual("设置门店会员卡号配置成功!", result['message'])


    def test_dock(self):
        result = configdata.create_dock()
        self.assertEqual("对接方新增成功", result['message'])
        dock_id = result['data']
        result = configdata.update_dock(dock_id)
        self.assertEqual("对接方修改成功", result['message'])
        result = configdata.delete_dock(dock_id)
        self.assertEqual("对接方删除成功", result['message'])




