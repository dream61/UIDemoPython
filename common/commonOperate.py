# coding=utf-8
__author__ = '刘影'
from selenium import webdriver
from common.webObject import webObject
from common.ScreenShot import saveScreenShot
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchFrameException,NoSuchWindowException,NoAlertPresentException,NoSuchElementException
from common.log import Log

log = Log()
class commonOperate():

    #def __init__(self,driver):
        #self.driver = driver
    def __init__(self,webObject):
        self.webObject = webObject

#单击元素
    def click(self, idpro, value):
        el = self.webObject.testEle(idpro=idpro,value=value)
        try:
            el.click()
            log.info("单击，根据对象{0}[{1}]，操作成功".format(idpro,value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("单击，根据对象{0}[{1}],单击失败,错误截图请见：{2}".format(idpro, value, screenshotdir))
            raise e
#输入操作
    def sendkey(self,idpro,value,inputv):
        el = self.webObject.testEle(idpro=idpro, value=value)
        try:
            el.clear()
            el.send_keys(inputv)
            log.info("输入，根据对象{0}[{1}]，输入成功".format(idpro, value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("输入，根据对象{0}[{1}],输入失败,错误截图请见：{2}".format(idpro, value,screenshotdir))
            raise e

#选择按选项的value值
    def selectValue(self,idpro,value,selectValue):
        el = self.webObject.testEle(idpro=idpro, value=value)
        try:
            s = Select(el)
            s.select_by_value(selectValue)
            log.info("按value值选择，根据对象{0}[{1}],选择成功".format(idpro, value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("按value值选择，根据对象{0}[{1}],选择失败,错误截图请见：{2}".format(idpro, value,screenshotdir))
            raise e
#选择按index
    def selectIndex(self,idpro,value,selectIndex):
        el = self.webObject.testEle(idpro=idpro, value=value)
        try:
            s = Select(el)
            s.select_by_index(selectIndex)
            log.info("按index值选择，根据对象{0}[{1}],选择成功".format(idpro, value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("按index值选择，根据对象{0}[{1}],选择失败,错误截图请见：{2}".format(idpro, value,screenshotdir))
            raise e
#选择按选项显示值
    def selectText(self,idpro,value,selectValue):
        el = self.webObject.testEle(idpro=idpro, value=value)
        try:
            s = Select(el)
            s.select_by_visible_text(selectValue)
            log.info("按显示文本选择，根据对象{0}[{1}],选择成功".format(idpro, value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("按显示文本选择，根据对象{0}[{1}],选择失败错误截图请见：{2}".format(idpro, value,screenshotdir))
            raise e
#取消对应index选项
    def deselectIndex(self,idpro,value,selectIndex):
        el = self.webObject.testEle(idpro=idpro, value=value)
        try:
            s = Select(el)
            s.deselect_by_index(selectIndex)
            log.info("取消按index选择，根据对象{0}[{1}],取消选择成功".format(idpro, value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("取消按index选择，根据对象{0}[{1}],取消选择失败,错误截图请见：{2}".format(idpro, value))
            raise e

    # 取消对应value选项
    def deselectValue(self, idpro, value, selectValue):
        el = self.webObject.testEle(idpro=idpro, value=value)
        try:
            s = Select(el)
            s.deselect_by_value(selectValue)
            log.info("取消按value选择，根据对象{0}[{1}],取消选择成功".format(idpro, value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("取消按value选择，根据对象{0}[{1}],取消选择失败,错误截图请见：{2}".format(idpro, value))
            raise e
    #取消对应文本选项
    def deselectText(self,idpro, value, selectValue):
        el = self.webObject.testEle(idpro=idpro, value=value)
        try:
            s = Select(el)
            s.deselect_by_visible_text(selectValue)
            log.info("取消按文本选择，根据对象{0}[{1}],取消选择成功".format(idpro, value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("取消按文本选择，根据对象{0}[{1}],取消选择失败,错误截图请见：{2}".format(idpro, value,screenshotdir))
            raise e
#鼠标悬停
    def mouseOn(self,idpro,value):
        el = self.webObject.testEle(idpro=idpro, value=value)
        try:
            actions = ActionChains(self.webObject.driver)
            actions.move_to_element(el)
            actions.perform()
            log.info("鼠标悬停，根据对象{0}[{1}],鼠标悬停成功".format(idpro, value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("鼠标悬停，根据对象{0}[{1}],鼠标悬停失败,错误截图请见：{2}".format(idpro, value,screenshotdir))
            raise e

#鼠标操作
    def mouseOperate(self,ovalue,idpro,value):
        el = self.webObject.testEle(idpro=idpro, value=value)
        try:
            actions = ActionChains(self.driver)
            if ovalue == "":
                screenshotdir = saveScreenShot(self.driver)
                log.error("鼠标操作，根据对象{0}[{1}],鼠标操作失败,错误截图请见：{2}".format(idpro, value,screenshotdir))
                raise AssertionError
            else:
                if ovalue == "左击":
                    actions.click(el).perform()
                if ovalue == "右击":
                    actions.context_click(el).perform()
                if ovalue == "双击":
                    actions.double_click(el).perform()
                log.info("鼠标点击，根据对象{0}[{1}],鼠标点击操作成功".format(idpro, value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("鼠标点击操作，根据对象{0}[{1}],鼠标点击操作失败,错误截图请见：{2}".format(idpro, value,screenshotdir))
            raise e

#鼠标拖拽
    def mouseDrag(self,idpro,value,target):
        el = self.webObject.testEle(idpro=idpro, value=value)
        try:
            target = self.webObject.testEle(idpro=idpro, value=target)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(el,target).perform()
            actions.release()
            log.info("鼠标拖拽，根据对象{0}[{1}],鼠标拖拽成功".format(idpro, value))
        except AssertionError as e:
            screenshotdir = saveScreenShot(self.driver)
            log.error("鼠标拖拽，根据对象{0}[{1}],鼠标拖拽失败,错误截图请见：{2}".format(idpro, value,screenshotdir))
            raise e

