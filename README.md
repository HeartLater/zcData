# zcData
# 运行前需要修改：
    1.conf文件
    2.index插入脚本中aus的ip
    3.定时任务
# 安装python2.7
    // 解压文件
    xz -d Python-2.7.13.tar.xz
    tar -xvf Python-2.7.13.tar

    // 进入解压后的文件夹
    cd Python-2.7.13
    // 运行配置
    ./configure --prefix=/usr/local
    // 编译和安装
    make
    make altinstall
# 需要的依赖
    elasticsearch
    urllib3
    setuptools
    //
    python2.7 setup.py install
