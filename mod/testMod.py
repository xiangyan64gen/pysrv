#coding:utf-8
#bach@330540504
#2019-06-11
from cls.BachMod import BachMod

class testMod(BachMod):
    def __init__(self):
        classname = format(type(self).__name__)
        self.dbname(classname)
        return 
    def lists(self):
        
        sql = 'select user_id from ysyy_user  limit 10';
        row1 = self.row(sql)

        return row1

    def __del__(self):
        print('del')
        self.close()
        return