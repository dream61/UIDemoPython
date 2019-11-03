#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:ASUS
# datetime:2019/10/27 20:00
# software: PyCharm
__author__ = '刘影'

import logging, time
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 日志目录
LOG_DIR = os.path.join(BASE_DIR,"logs")
# 日志存放文件夹，如不存在，则自动创建一个logs目录
if not os.path.exists(LOG_DIR):os.mkdir(LOG_DIR)

class Log():
    """
    日志记录类
    """
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(LOG_DIR, '%s.log'%time.strftime('%Y-%m-%d %H_%M_%S'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] [%(filename)s|%(funcName)s] [line:%(lineno)d] %(levelname)-8s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地日志文件
        fh = logging.FileHandler(self.logname,encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)