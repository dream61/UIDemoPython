#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = '刘影'
import os,sys
import time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
from selenium import webdriver

def saveScreenShot(driver):
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filePath = setting.TEST_REPORT + "/screenshot/"
    imgn = now + ".png"
    driver.get_screenshot_as_file(filePath+imgn)
    return imgn