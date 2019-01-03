#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from elasticsearch import Elasticsearch

class FileMonitor(object):
    """docstring for FileMonitor"""
    def __init__(self, file_path='', record_file='file.record', elastic={}):
        super(FileMonitor, self).__init__()
        self.file_path = file_path
        self.record_file = record_file
        self.ts_header = {

        },
        self.es = Elasticsearch(elastic.host)

    def file_monitor(self):
        """记录目标文件夹下当前文件"""
        with open(self.record_file,'w') as f:
            f.close()
        for root, dirs, files in os.walk(self.file_path):
            for name in files:
                create_time = os.stat(name).st_mtime
                with open(self.record_file, 'wa') as f:
                    f.write(':'.join('%s' % name, '%s\n' % create_time))
                    f.close()

    def new_file(self):
        """判断是否有新增文件，有则返回"""
        # 读取历史记录
        record_dict = {}
        record = open(self.record_file, 'r').readlines()
        for row in record:
            (key, value) = row.split(':')
            record_dict[key] = value
        # 遍历目标文件夹
        for root, dirs, files in os.walk(self.file_path):
            # 这里只关心是否有新增文件，并不管是否有修改
            # 因此只需要比较字典是否包含，不需要比较文件更改时间
            for name in files:
                if not record_dict.has_key(name):
                    # 调用数据处理，或者可以复制该文件到其他地方处理
                    self.file_handler(name)

    def file_handler(self, name):
        """新增文件处理"""
        pass
