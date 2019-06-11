# -*- coding: utf-8 -*-
#bach@330540504
#2019-06-11
import mysql.connector

class BachDB():
    dbname = None
    db_host = None
    db_port = None
    db_name = None
    db_user = None
    db_pwd = None
    cur = None
    con = None
    def __init__(self,dbname = 'sanhao'):
        self.dbname = dbname
        self.dbSwitch(self.dbname)
        self.connect()
        return
    def connect(self):
        try:
            self.con = mysql.connector.connect(host = self.db_host, user = self.db_user, password = self.db_pwd, port = self.db_port, database = self.db_name)            
            self.cur = self.con.cursor(buffered=True)
        except Exception as err:
            print(err)
            return False
        return
    def close(self):
        '''结束查询和关闭连接'''
        try:
            self.cur.close()
            self.con.close()
        except Exception as err:
            print(err)
            return False
        return

    def create_table(self,sql_str):
        '''创建数据表'''
        try:
            return self.cur.execute(sql_str)
        except Exception as e:
            print(e)
            return False
    def row(self,sql_str,rs_type=1):
        '''查询单条数据
        '''
        try:
            self.cur.execute(sql_str)
            row = self.cur.fetchone()  
            if rs_type == 1:
                col = self.cur.column_names
                row= dict(zip(col,row))
            return row
        except Exception as err:
            print(err)
            return False
    def rows(self,sql_str,rs_type=1):
        '''查询数据，返回一个列表，里面的每一行是一个字典，带字段名
             cursor 为连接光标
             sql_str为查询语句
        '''
        try:
            self.cur.execute(sql_str)
            rows = self.cur.fetchall()
            if rs_type == 1:
                r = []
                for x in rows:
                    r.append(dict(zip(self.cur.column_names,x)))
                rows = r
            return rows
        except Exception as err:
            print(err)
            return False

    def exec(self,sql):
        '''
        插入或更新记录 成功返回总数
        '''
        try:
            self.cur.execute(sql)
            self.con.commit()
            # return self.cur.lastrowid
            return self.cur.rowcount
        except Exception as err:
            print(err)
            return False

    def dbSwitch(self,dbname='sanhao'):
        import configparser
        import os
        cf = configparser.ConfigParser()
        path = os.getcwd()
        cf.read(path+"/config/DB.conf")
        dbinfo = cf.sections()
        is_db = False
        for var in dbinfo:
            is_db = dbname.startswith(var)
            if is_db:
                dbname = var
                break
        if is_db == False:
            dbname = 'sanhao'
        self.db_host = cf.get(dbname,'db_host')
        self.db_port = cf.get(dbname,'db_port')
        self.db_name = cf.get(dbname,'db_name')
        self.db_user = cf.get(dbname,'db_user')
        self.db_pwd = cf.get(dbname,'db_pwd')
        return 