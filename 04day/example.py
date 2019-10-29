# 1. 统计系统当前运行的进程数
# ps aux | grep java | grep -v grep | wc -l

# 2. 编写一个脚本, 输出脚本所在的路径
# echo $PWD

# 3. 书写一个脚本, 显示系统当前日期和时间
# echo $(date +%Y-%m-%d_%H:%M:%S)

# 4. 请编写一个脚本将/opt/hatech.log文件备份至/tmp下, 备份的文件名带上当前系统时间
# cp /opt/hatech.log /tmp/hatech.log-$(date +%Y%m%d%H%M%S)

# 5. 请使用一条指令检索当前服务器上所有的Java进程, 并批量关闭不区分大小写
# java_pid = $(ps aux | egrep [Jj][aA][vV][aA] | grep -v grep | awk '{ print $2 }')
# for pid in ${java_pid}; do
#     kill -9 pid
# done

# 6. 将hatech.txt文件中的tab符,都替换成|
# sed -ie "s/\t/|/g" hatech.txt

# 7. 批量修改名称, 后缀修改为大写
import os

for files in os.listdir('./'):
    print(
        os.path.join(
            os.path.splitext(files)[0],
            os.path.splitext(files)[1].upper()).replace('/', '')
    )

# 8. 写出你常用的10个python模块, 体现python深度
# subprocess, psutil, paramiko, echarts, random
# re, logging, os, 


