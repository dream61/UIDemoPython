# coding=utf-8
__author__ = '刘影'
from selenium import webdriver
from common.log import Log
log = Log()
class BrowserOperate:
    def __init__(self, driver):
        self.driver = driver
    #打开浏览器
    def openUrl(self,url):
        self.driver.get(url)
        log.info("打开网址{0}成功".format(url))
    #全局等待
    def forceGlobalWait(self, implicitlytime, pageLoadtime, setScripttime):
        self.driver.implicitly_wait(int(implicitlytime))
        self.driverl.implicitly_wait(int(pageLoadtime))
        self.driver.implicitly_wait(int(setScripttime))
    #页面加载
    def pageLoadtime(self, pageLoadtime):
        self.driver.implicitly_wait(int(pageLoadtime))
    #关闭当前页
    def closeCurrentBr(self):
        i = self.driver.window_handles
        if i == 1:
            self.driver.close()
        else:
            self.driver.close()
            handles = self.driver.window_handles
            self.driver.switch_to_window(handles[-1])
    #切换到最后一个窗口
    def swithLastBr(self):
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
    #最大化窗口
    def maxwindow(self):
        self.driver.maximize_window()