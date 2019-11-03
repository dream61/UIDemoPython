#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = '刘影'

from common.log import Log
import yaml
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
log = Log()

def getYamlData(filepath):
    # 读取yaml的值
    try:
        yamlindex = open(filepath, 'r', encoding='utf-8')
        # 把文件内容读取出来
        data = yaml.load(yamlindex, Loader=yaml.FullLoader)
        return data
    except FileNotFoundError as yamlindex:
        log.error("文件不存在：{0}".format(yamlindex))

