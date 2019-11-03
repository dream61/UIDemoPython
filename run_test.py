#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:ASUS
# datetime:2019/10/23 20:38
# software: PyCharm
__author__ = '刘影'
import unittest,time
import os,sys
sys.path.append(os.path.dirname(__file__))
import HTMLTestRunner
from common.sendemail import send_mail
from common.getreport import new_report
from config import setting

# 测试报告存放文件夹，如不存在，则自动创建一个report目录
if not os.path.exists(setting.TEST_REPORT):
    os.makedirs(setting.TEST_REPORT + '/' + "screenshot")

def add_case(test_dir=setting.TEST_DIR):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test2.py')

    return discover
def run_case(all_case,resultPath=setting.TEST_REPORT):
    """执行所有的测试用例"""
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = resultPath + '/' + now + '_result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title="UI自动化测试报告",
        description="测试报告的详情")
    runner.run(all_case)
    fp.close()
    report = new_report(setting.TEST_REPORT)  # 调用模块生成最新的报告
    send_mail(report)  # 调用发送邮件模块
if __name__ == "__main__":
    cases = add_case(setting.TEST_DIR)
    run_case(cases)


