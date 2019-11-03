# coding=utf-8
import unittest
import time,os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from selenium import webdriver
from common.DriverManage import DriverManage
from common.BrowserOperate import BrowserOperate
from common.commonOperate import commonOperate
from common.webObject import webObject
from common.CheckAssert import checkAssert
import HTMLTestRunner



class t123(unittest.TestCase):
    driver = DriverManage.initDriver("chrome")
    br = BrowserOperate(driver)
    wb = webObject(driver)
    cn = commonOperate(driver)
    ck = checkAssert(driver,cn)
    def setUp(self):
        base_url = "http://www.baidu.com"
        BrowserOperate(self.driver).openUrl(base_url)
    def test_op(self):
        commonOperate(self.driver).sendkey("id","kw","测试")
        self.cn.click("id","su")
        #self.ck.checkText("class","toindex","text","百度首页")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='自动化测试UI报告',description='Implementation Example with:')
    runner.run()
    fp.close()

