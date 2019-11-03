#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = '刘影'
import pymysql
from common.log import Log
log = Log()

class database:
    def connectData(self,datatype,server,user,pwd,dataname):
        if datatype.lower() == "mysql":
            conn = pymysql.connect(server,user,pwd,dataname,charset="utf8")
            return conn
        if datatype.lower() == "oracle":
            pass
        else:
            log.error("不存在此数据库！")

    #查询数据库单条数据
    def executeSql(self,datatype,server,user,pwd,dataname,sqlstr):
        conn = self.connectData(datatype,server,user,pwd,dataname)
        cur = conn.cursor()
        cur.execute(sqlstr)
        rows = cur.fetchone() #获取第一条数据
        conn.close()
        log.info("数据库单条查询操作成功")
        return rows

#查询多条数据
    def executeSqlAll(self,datatype,server,user,pwd,dataname,sqlstr):
        conn = self.connectData(datatype, server, user, pwd, dataname)
        cur = conn.cursor()
        cur.execute(sqlstr)
        results = cur.fetchall()
        li = []
        for result in results:
            li.append(result)
        print(li)
        conn.commit()
        conn.close()


