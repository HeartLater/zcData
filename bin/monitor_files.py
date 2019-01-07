#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import datetime


class FileMonitor(object):
    """docstring for FileMonitor"""
    def __init__(self, file_path='', record_file='file.record', elastic={}, original_file_path=''):
        super(FileMonitor, self).__init__()
        self.original_file_path = original_file_path
        self.file_path = file_path
        self.record_file = record_file
        # self.ts_header = ['time','batch_no','track_target_kind','track_target_type','attribute','nationality','order','dynamic','high','longitude','latitude','distance_x','distance_y','velocity_x','velocity_y','track_time','bearing','velocity_h','threat_cla','threat_time','battle_state','flag']
        self.es = Elasticsearch(hosts=elastic['host'], port=elastic['port'], timeout=elastic['timeout'])
        self.ts_header_TYTSMB = ['time','batch_no','track_target_kind','track_target_type','attribute','nationality','order','dynamic','high','longitude','latitude','distance_x','distance_y','velocity_x','velocity_y','track_time','bearing','velocity_h','threat_cla','threat_time','battle_state','flag']
        self.ts_header_YSHJXX = ['time','trs_plat_station_no','track_target_kind','track_target_type','fight_state','attribute','track_target_num','nationality','order','dynamic','cooperate_station_no','bearing_precision','distance_precision','depth','depth_precision','high_precision','sys_batch_no','batch_no','high','longitude','latitude','distance_x','distance_y','velocity_x','velocity_y','time2','bearing','velocity_h']

    def filter_files(self):
        file_list = []
        for root, dirs, files in os.walk(self.original_file_path):
            for file_name in files:
                if 'dat' in file_name:
                    file_list.append(file_name)
        for end_file_name in file_list:
            print end_file_name
        return file_list


    def split_files(self,files_name_list):
        for file_name in files_name_list:
            new_file_name_YSHJXX = "BDtaishi.YSHJXX." + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".dat"
            new_file_name_TYTSMB = "BDtaishi.TYTSMB." + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".dat"
            with open(self.original_file_path + "/" + file_name, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if "YSHJXX" in line:
                        fo1 = open(self.file_path + "/" + new_file_name_YSHJXX, 'a')
                        str_list1 = line.split(',')[8:]
                        str1 = ",".join(str_list1)
                        fo1.write(str1)
                        fo1.close()
                    elif "TYTSMB" in line:
                        fo2 = open(self.file_path + "/" + new_file_name_TYTSMB, 'a')
                        str_list2 = line.split(',')[8:]
                        str2 = ",".join(str_list2)
                        fo2.write(str2)
                        fo2.close()
                    else:
                        pass

    def file_monitor(self):
        # 调用函数处理原始文件，将文件处理后导入file_path中，供给feed插入hive，供给下面程序插入aus
        file_list = self.filter_files()
        self.split_files(file_list)
        # with open(self.record_file,'w') as f:
        #     f.close()
        # 跟上次记录历史对比，判断是否有新增文件
        record_dict = {}
        record = open(self.record_file, 'r').readlines()
        for row in record:
            (key, value) = row.split(':')
            record_dict[key] = value
        # 遍历目标路径
        for root, dirs, files in os.walk(self.file_path):
            # 这里只关心是否有新增文件，并不管是否有修改
            # 因此只需要比较字典是否包含，不需要比较文件更改时间
            for name in files:
                print "all files name:" + name
                if record_dict.has_key(name):
                    continue
                if 'TYTSMB' in name or 'YSHJXX' in name:
                    print "the file will be input:" + name
                    # 调用数据处理，或者可以复制该文件到其他地方处理
                    self.file_handler(root=root, name=name)
                # if not record_dict.has_key(name):
                #     print "the file will be input:" + name
                #     self.file_handler(root=root, name=name)
    def file_handler(self, root='', name=''):
        """新增文件处理"""
        # 将文件复制到feed路径
        filepath = os.path.join(root, name)
        # os.system('cp ' + filepath + ' /var/dropzone')
        os.system('scp ' + filepath + ' 10.0.37.159:/var/dropzone')
        create_time = os.stat(os.path.join(root, name)).st_mtime
        # 将 文件名:创建时间 追加到记录文件
        with open(self.record_file, 'a') as f:
            f.write('%s:%s\n' % (name, create_time))
            # f.write(':'.join('%s' % name, '%s\n' % create_time))
            f.close()
        index_name = "_".join(name.lower().split(".")[0:2])  # 确定索引名称
        if not self.es.indices.exists(index=index_name):
            self.create_index(index_name, index_name)
        actions = []
        for line in open(os.path.join(root, name)):
            source = {}
            fields = line.split(',')
            # 根据索引名确定使用哪个header
            if 'TYTSMB' in name:
                ts_header = self.ts_header_TYTSMB
            else:
                ts_header = self.ts_header_YSHJXX

            for i in range(len(ts_header)):
                source[ts_header[i]] = fields[i]
            action = {
                '_index': index_name,
                '_type': index_name,
                '_source': source
            }
            actions.append(action)
            if len(actions) > 5000:
                success, _ = bulk(self.es, actions)
                actions = []
        if actions:
            success, _ = bulk(self.es, actions)
            print success

    def create_index(self, index_name, index_type):

        if 'tytsmb' in index_name:
            res = os.system("sh ./create_tytsmb_index.sh")
            print res
            # ts_header = self.ts_header_TYTSMB
        else:
            res = os.system("sh ./create_yshjxx_index.sh")
            print res
            # ts_header = self.ts_header_YSHJXX
        # """创建索引"""
        # # 映射
        # _index_mappings = {
        #     'mappings': {
        #         'index_type': {
        #             'properties': {}
        #         }
        #     }
        # }
        # _type = {'type': 'string'}
        # for item in ts_header:
        #     _index_mappings['mappings']['index_type']['properties'][item] = _type
        # res = self.es.indices.create(index=index_name, body=_index_mappings)
        # # print res
