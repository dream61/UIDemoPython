# coding=utf-8
__author__ = '刘影'
from selenium import webdriver
from common.webObject import webObject
from common.log import Log
import HTMLTestRunner
log = Log()

class checkAssert:
    def __init__(self, webObject):
        self.webObject = webObject

    def checkText(self,idpro,value,checkvar,expectvar):
        el = self.webObject.testEle(idpro,value)
        try:
            if "text" == checkvar:
                s1 = el.text
                if s1 == expectvar:
                    log.info("检查文本，根据对象{0}[{1}]，与期望值[{2}]一致".format(idpro,value,expectvar))
                else:
                    log.error("检查文本，根据对象{0}[{1}]，与期望值[{2}]不一致".format(idpro, value,expectvar))
                    raise AssertionError
            else:
                s1 = el.get_attribute(expectvar)
                if s1 == expectvar:
                    print('预期值与期望值一致')
                else:
                    print('预期值与期望值不一致')
        except AssertionError as e:
            log.error("根据对象{0}页面中未能找到{1}元素,检查属性失败".format(idpro,value))
            raise e



