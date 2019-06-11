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
        var = '开始test'
        self.echo(var)
        # self.parentMethod()
        row1 = self.mod.lists();
        if row1 :
            print(row1.get('u_id'))
        # for var in row:
        #     print(var['u_id'])
        print(row1)

        sql = 'select * from ysyy_user limit 1'
        row = self.mod.row(sql)
        print(row)
        self.log(111)
        # sql = 'update buz_user set data_status = 2 where user_id = 971;'
        # rs = self.exec(sql)
        # print(rs)
        return ;