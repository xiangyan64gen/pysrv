#coding:utf-8
#bach@330540504
#2019-06-11
#自动生成文件
import os
class pro:
    root = None
    filelists = []
    doc = ''
    bakfile = []
    def __init__(self):
        print('===启动自动生成文件程序===')
        self.root = os.getcwd()
        return
    def pro(self,appname='None',doc=''):
        self.doc = doc
        if appname=='None':
            print('请配置项目名称！')
            return
        #1.创建文件
        #2.修改文件

        iscr = self.cr(appname)
        if iscr == False:
            return
        self.ed(appname)

        pass
    def cr(self,appname):
        print('创建文件中')
        print('--------------------------')
        #1.1 根目录
        cr1 = self.create(appname)
        #1.2 app目录
        cr2 = self.create(appname,crType='App')
        #1.3 Mod目录
        cr3 = self.create(appname,crType='Mod')
        if cr1 & cr2 & cr3:
            print('--------------------------')
            print('文件创建成功')
            print('--------------------------')
            return True
        else:
            print('--------------------------')
            print('文件创建失败')
            print('--------------------------')
            return False
        pass
    def create(self,appname,crType=''):
        file = self.getPath(appname,crType)
        if not os.path.exists(file):
            os.mknod(file)
            print('已创建文件：' + file)
            return True
        else:
            # os.remove(file)
            print('该文件已存在！' + file)
            return False
    def getPath(self,appname,crType):
        
        if crType != '':
            appname = self.getAppName(appname,crType)
            crType = crType.lower()
            file = self.root + '/'+crType+'/' + appname + '.py'
        else:
            file = self.root + '/' + appname + '.py'
        self.filelists.append(file) 
        return file
    def getAppName(self,appname,crType=''):
        appname = appname + crType
        return appname

    def ed(self,appname = ''):
        print('修改文件开始')
        print('■■■■■■■■■■■■■■■■■■■■■■■ ok!')
        num = [0,1,2]
        for i in num:
            self.fileEdit(i,appname)
        print('修改文件结束')
        print('--------------------------')
        return
    def fileEdit(self,i,appname):

        self.bakfile = self.getPathTm()
        op = open(self.bakfile[i],'r')
        bakTest = op.read()
        appnameapp = self.getAppName(appname,'App')
        appnamemod = self.getAppName(appname,'Mod')
        bakTest = bakTest.replace('testApp',appnameapp)
        bakTest = bakTest.replace('testMod',appnamemod)
        import time
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        bakTest = bakTest.replace('time',nowTime)
        bakTest = bakTest.replace('doc',self.doc)
        op.close()
        op = open(self.filelists[i],'r+')
        op.write(bakTest)
        op.close()
        return 
    def getPathTm(self):
        file = []
        file1 = self.root + '/ext/pro/template/'+ 'test.py'
        file2 = self.root + '/ext/pro/template/'+ 'testApp.py'
        file3 = self.root + '/ext/pro/template/'+ 'testMod.py'
        file.append(file1)
        file.append(file2)
        file.append(file3)
        return file
    def __del__(self):
        print('===结束自动生成文件程序===')
        pass