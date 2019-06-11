#coding:utf-8
#bach@330540504
#2019-06-11
import fun.fun as fun
from ext.log.log import log

class Bach:        # 定义父类

    db = None

    def __init__(self):
        return
    def parentMethod(self):
        print('调用父类方法')
        # self.ceshi(123)
        return
    def log(self,arg=None):
        arg = str(arg)
        log(arg)
        return
    def echo(self,arg=None,type=1):
        print(arg)
        if type==1:
            self.log(arg)
        return