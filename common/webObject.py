# coding=utf-8
__author__ = '刘影'
from selenium import webdriver
from common.ScreenShot import saveScreenShot
from common.log import Log

log = Log()

class webObject():
    def __init__(self,driver):
        self.driver = driver

    def getDriver(self):
        return self.driver

    # 定位查找元素
    def testEle(self,idpro,value):
        try:
            if idpro.lower() == "id":
                el = self.driver.find_element_by_id(value)
            elif idpro.lower() == "xpath":
                el = self.driver.find_element_by_xpath(value)
            elif idpro.lower() == "class":
                el = self.driver.find_element_by_class_name(value)
            elif idpro.lower() == "css":
                el = self.driver.find_element_by_css_selector(value)
            elif idpro.lower() == "tagname":
                el = self.driver.find_element_by_tag_name(value)
            elif idpro.lower() == "linktext":
                el = self.driver.find_element_by_link_text(value)
            else:
                print("类型错误")
        except Exception as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("定位元素，根据对象{0}[{1}]定位失败,错误截图请见：{2}".format(idpro, value,screenshotdir))
            raise e
        return el
#定位一组元素
    def findElements(self,idpro,value):
        if idpro.lower() == "id":
            el = self.driver.find_elements_by_id(value)
        elif idpro.lower() == "xpath":
            el = self.driver.find_elements_by_xpath(value)
        elif idpro.lower() == "class":
            el = self.driver.find_elements_by_class_name(value)
        elif idpro.lower() == "css":
            el = self.driver.find_elements_by_css_selector(value)
        elif idpro.lower() == "tagname":
            el = self.driver.find_elements_by_tag_name(value)
        elif idpro.lower() == "linktext":
            el = self.driver.find_elements_by_link_text(value)
        else:
            print("类型错误")
        return el