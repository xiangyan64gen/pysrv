#!/usr/bin/python3
#coding:utf-8
import os
import time

def log(msg="error"):
    msg = str(msg)
    ROOT = os.getcwd()
    filename = time.strftime("%Y_%m_%d", time.localtime()) + ".log"

    pa = ROOT+"/log/"
    fl = pa + filename

    is_file = os.path.exists(pa)
    if not is_file:
        # print("创建")
        #pa = pa.rstrip("/")
        os.makedirs(pa)
    fo = open(fl,"a+")

    fo.write(msg+"\r\n")
    fo.close
    # print("log记录成功")
    return

# log("白不白")