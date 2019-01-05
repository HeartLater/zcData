#!/bin/bash
# @author: Yampery
basepath=$(cd `dirname $0`; pwd)
cd $basepath
if [ !$1 ] || [ $1 == "start" ]; then
    time=$(date "+%Y-%m-%d_%H_%M_%S") 
    nohup python2 -u bin/run.py $2 > logs/console.log.$time 2>&1 &
    echo "$!" > pid
elif [ $1 == "stop" ]; then
    kill `cat pid`
else
    echo "Please use [start, stop]"
fi
