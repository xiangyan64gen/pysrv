#coding:utf-8
#bach@330540504
#2019-06-11
from cls.BachMod import BachMod

class indexMod(BachMod):
    def __init__(self):
        classname = format(type(self).__name__)
        self.dbname(classname)
        return 
    def lists(self):
        print('hello BachMod!!!')
        return

    def __del__(self):
        self.close()
        return