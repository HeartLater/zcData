#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: Admin 
@file: split_source_files.py
@time: 2019/1/3 0003
"""
import os

import datetime


class Main():
    def __init__(self):
        pass

def filter_files(path):
    file_list = []
    for root,dirs,files in os.walk(path):
        for file_name in files:
            if 'dat' in file_name:
                file_list.append(file_name)
    for end_file_name in file_list:
        print end_file_name
    return file_list

def split_files(files_name_list,path):
    for file_name in files_name_list:
        new_file_name_YSHJXX = "BDtaishi.YSHJXX." + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".dat"
        new_file_name_TYTSMB = "BDtaishi.TYTSMB." + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".dat"
        ys_list = []    # 写入YSHJXX
        ty_list = []    # 写入TYTSMB
        with open(path + "/" + file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "YSHJXX" in line:
                    str_list1 = line.split(',')[8:]
                    str1 = ",".join(str_list1)
                    ys_list.append(str1)

                elif "TYTSMB" in line:
                    str_list2 = line.split(',')[8:]
                    str2= ",".join(str_list2)
                    ty_list.append(str2)
                else:
                    pass
            # 循环结束，判断连个list如果不为空，则打开相应的文件将list追加进文件
            if ys_list:
                with open(path + "/" + new_file_name_YSHJXX, 'a') as f:
                    f.writelines(ys_list)
            if ty_list:
                with open(path + "/" + new_file_name_TYTSMB, 'a') as f:
                    f.writelines(ty_list)


if __name__ == '__main__':
    path = "/xdata/zcData/sourceFiles/MSGDAT/Ts"
    files_name_list = filter_files(path)
    split_files(files_name_list,path)