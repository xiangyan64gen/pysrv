#!/usr/bin/python3
#coding:utf-8
#bach@330540504
#2019-06-11

from app.testApp import testApp



i = testApp()
i.test()

# from cls.BachDB import BachDB
# db = BachDB(dbname = 'buz')
# sql = 'select u_id,user_id from buz_user  limit 10';
# rows = db.rows(sql);
# print(rows)
# sql = 'select u_id from buz_service  limit 10';
# row = db.rows(sql);
# print(row)