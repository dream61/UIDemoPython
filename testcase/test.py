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


    def setUp(self):
        base_url = "http://www.baidu.com"
        self.br.openUrl(base_url)

    def test_op(self):
        u'''测试百度搜索'''
        self.cn.sendkey("id", "kw", getYamlData(self.ydata)['case1']['test'])
        self.cn.click("id", "su")
        self.ck.checkText("class","toindex","text","百度首页")
        #self.ex.writeCell("F:\\GitStudy\\UIDemoPython\\testdata\\book_list.xlsx","个人管理",2,2,"用所有的存在与世界相会_自动化测试写入")
        #self.ex.readCell("F:\\GitStudy\\UIDemoPython\\testdata\\book_list.xlsx","个人管理",2,2)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


