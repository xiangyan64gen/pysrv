#coding:utf-8
#bach@330540504
#2019-06-11
from cls.Bach import Bach
from mod.testMod import testMod

class testApp(Bach):
    mod = None
    def __init__(self):
        self.mod = testMod()
        return ;
    def WorkerStart(self):
        print('hello Bach!!!')
        self.mod.lists()
        return ;