# encoding: utf-8
"""
使用多个数据源得到公网IP地址
"""

from urllib2 import urlopen
from json import load
import re
from datetime import datetime
import time
timeout = 3

def get_pub_ip():
    """得到本机公网IP地址"""
    try:
        pub_ip = urlopen('http://ip.42.pl/raw', timeout=timeout).read()
        if judge_legal_ip(pub_ip):
            return pub_ip
    except:
        pass


    try:
        pub_ip = urlopen('http://ifconfig.me', timeout=timeout).read()
        if judge_legal_ip(pub_ip):
            return pub_ip
    except:
        pass

    try:
        pub_ip = load(urlopen('http://httpbin.org/ip',timeout=timeout))['origin']
        if judge_legal_ip(pub_ip):
            return pub_ip
    except:
        pass

    try:
        pub_ip = load(urlopen('https://api.ipify.org/?format=json', timeout=timeout))['ip']
        if judge_legal_ip(pub_ip):
            return pub_ip
    except:
        pass

    return  "" # 没有获取正确的IP地址


def judge_legal_ip(ip):
    """判断一个IP地址是否合法"""
    compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if compile_ip.match(ip):
        return True
    else:
        return False


def main():
    public_ip = get_pub_ip()
    print datetime.now().strftime("%Y-%m-%d %H:%M:%S"), public_ip


if __name__ == '__main__':
    # main()
    while 1:
        main()
        time.sleep(5)
