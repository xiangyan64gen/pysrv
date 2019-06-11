#coding:utf-8
#bach@330540504
#2019-06-11
from cls.Bach import Bach
from mod.indexMod import indexMod

class indexApp(Bach):
    mod = None
    def __init__(self):
        self.mod = indexMod()
        return ;
    def WorkerStart(self):
        print('hello Bach!!!')
        self.mod.lists()
        return ;