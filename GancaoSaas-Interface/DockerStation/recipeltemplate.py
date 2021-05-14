from DockerStation import recipeltemplatedata
import unittest
import random

class Recipeltemplate(unittest.TestCase):

    random = random.randint(1111, 9999)
    templatename = "模版名称" + str(random)

    def test_create_recipeltemplate(self):
        result = recipeltemplatedata.create_recipeltemplate_cloud(self.templatename, 1)
        self.assertEqual("添加药方模板成功", result['message'])
        cloud_template_id = result['data']
        result = recipeltemplatedata.update_recipeltemplate_cloud(self.templatename, cloud_template_id, 1)
        self.assertEqual("修改药方模板成功", result['message'])
        result = recipeltemplatedata.create_recipeltemplate_zhongyao(self.templatename, 1)
        self.assertEqual("添加药方模板成功", result['message'])
        zhongyao_template_id = result['data']
        result = recipeltemplatedata.update_recipeltemplate_zhongyao(self.templatename, zhongyao_template_id, 1)
        self.assertEqual("修改药方模板成功", result['message'])
        result = recipeltemplatedata.create_recipeltemplate_chengyao(self.templatename, 1)
        self.assertEqual("添加药方模板成功", result['message'])
        chengyao_template_id = result['data']
        result = recipeltemplatedata.update_recipeltemplate_chengyao(self.templatename, chengyao_template_id, 1)
        self.assertEqual("修改药方模板成功", result['message'])
        result = recipeltemplatedata.create_recipeltemplate_qixie(self.templatename, 1)
        self.assertEqual("添加药方模板成功", result['message'])
        qixie_template_id = result['data']
        result = recipeltemplatedata.update_recipeltemplate_qixie(self.templatename, qixie_template_id, 1)
        self.assertEqual("修改药方模板成功", result['message'])
        result = recipeltemplatedata.create_recipeltemplate_item(self.templatename, 1)
        self.assertEqual("添加药方模板成功", result['message'])
        item_template_id = result['data']
        result = recipeltemplatedata.update_recipeltemplate_item(self.templatename, item_template_id, 1)
        self.assertEqual("修改药方模板成功", result['message'])
        result = recipeltemplatedata.create_recipeltemplate_cloud(self.templatename, 2)
        self.assertEqual("添加药方模板成功", result['message'])
        result = recipeltemplatedata.create_recipeltemplate_zhongyao(self.templatename, 2)
        self.assertEqual("添加药方模板成功", result['message'])
        result = recipeltemplatedata.create_recipeltemplate_chengyao(self.templatename, 2)
        self.assertEqual("添加药方模板成功", result['message'])
        result = recipeltemplatedata.create_recipeltemplate_qixie(self.templatename, 2)
        self.assertEqual("添加药方模板成功", result['message'])
        result = recipeltemplatedata.create_recipeltemplate_item(self.templatename, 2)
        self.assertEqual("添加药方模板成功", result['message'])


