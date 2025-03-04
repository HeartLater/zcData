#!/usr/bin/env python
# encoding: utf-8

import sys
import json
from monitor_files import FileMonitor


def main():
    """文件监控入口
    """
    config_file = ''
    if len(sys.argv) >= 2:
        config_file = sys.argv[1]
    else:
        config_file = '../conf/config.json'

    with open(config_file, 'r') as jsonfile:
        config = json.load(jsonfile)

    monitor = FileMonitor(file_path=config['path'], elastic=config['elastic'], original_file_path=config['original_path'])
    # 监控目标路径
    monitor.file_monitor()


if __name__ == "__main__":
    main()
