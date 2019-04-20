# encoding:utf-8

"""
通过ping命令，测试主机的网络环境
"""

import re
import os
import subprocess
import sys
import time
from datetime import datetime


def ping(host):
    os_name = os.name
    # 根据系统平台设置 ping 命令
    if os_name == 'nt':  # windows
        cmd = 'ping ' + host
    else:  # unix/linux
        cmd = 'ping -c 5 ' + host

    # 执行 ping 命令
    sub = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, shell=True)
    out = sub.communicate()[0]
    if not out:
        return host, '0.0.0.0', 0, 100

    # 替换换行符，因为在正则表达式中
    # 'a$' 匹配 'a\r\n' 中的 'a\r'
    text = out.replace('\r\n', '\n').replace('\r', '\n')

    # 使用正则匹配 ip 地址: [192.168.1.1] (192.168.1.1)
    ip = re.findall(r'(?<=\(|\[)\d+\.\d+\.\d+\.\d+(?=\)|\])', text)

    # 获取时间信息
    if os_name == 'nt':
        time = re.findall(r'\d+(?=ms$)', text)
    else:
        time = re.findall(r'(?<=\d/)[\d\.]+(?=/)', text)

    # 丢包率
    lost = re.findall(r'\d+(?=%)', text)

    ip = ip[0] if ip else '0.0.0.0'

    # 小数点四舍五入
    time = int(round(float(time[0]))) if time else 0
    lost = int(round(float(lost[0]))) if lost else 0

    return host, ip, time, lost


if __name__ == '__main__':
    print '探测时间','目标','IP','时延时间','丢包率'

    while 1:
        domain = 'www.baidu.com'
        domain,ip,duration_time,lost = ping(domain)
        print  datetime.now().strftime("%Y-%m-%d %H:%M:%S"), domain,ip,duration_time,lost
        domain = 'whois.verisign-grs.com'
        domain, ip, duration_time, lost = ping(domain)
        print  datetime.now().strftime("%Y-%m-%d %H:%M:%S"), domain, ip, duration_time, lost
        time.sleep(2)
