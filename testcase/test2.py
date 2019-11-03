# coding=utf-8
__author__ = '刘影'
import unittest
from common.readYamlData import getYamlData
from common.DriverManage import DriverManage
from common.BrowserOperate import BrowserOperate
from common.commonOperate import commonOperate
from common.webObject import webObject
from common.CheckAssert import checkAssert
from common.excelOperate import ExcelOperate
from config import setting

class test(unittest.TestCase):
    driver = DriverManage.initDriver("chrome")
    br = BrowserOperate(driver)
    wb = webObject(driver)
    cn = commonOperate(wb)
    ck = checkAssert(wb)
    ex = ExcelOperate()
    ydata = setting.TEST_DATA_YAML + "/" + "baidu.yaml"
    edata = setting.TEST_Element_YAML + "/" + "element.yaml"

    @classmethod
    def setUpClass(cls):
        base_url = "http://www.baidu.com"
        cls.br.openUrl(getYamlData(cls.edata)['weburl']['url'])


    def test_op(self):
        u'''测试达达影院首页'''
        self.cn.click(getYamlData(self.edata)['indexp'][0]['find_type'],
                      getYamlData(self.edata)['indexp'][0]['element_info'])
        self.cn.sendkey(getYamlData(self.edata)['indexp'][2]['find_type'],
                      getYamlData(self.edata)['indexp'][2]['element_info'],getYamlData(self.edata)['indexp'][2]['info'])

    def test_ddt(self):
        u'''测试达达影院电影界面'''
        self.cn.click(getYamlData(self.edata)['indexp'][1]['find_type'],getYamlData(self.edata)['indexp'][1]['element_info'])

    @classmethod
    def tearDownClass(cls):
        #self.driver.refresh()
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()