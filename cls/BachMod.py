#coding:utf-8
#bach@330540504
#2019-06-11
import fun.fun as fun
from ext.log.log import log
from cls.BachDB import BachDB
from cls.Bach import Bach

class BachMod(Bach):        # 定义父类

    db = None

    def __init__(self):
        return
    def dbname(self,dbname='sanhao'):
        self.db = BachDB(dbname)
        return
    def row(self,sql,rs_type=1):
        row = self.db.row(sql,rs_type)
        return row 
    def rows(self,rs_type=1):
        rows = self.db.rows(sql,rs_type)
        return rows
    def exec(self,sql):
        rows = self.db.exec(sql)
        return rows 
    def close(self):
        self.db.close()
        return