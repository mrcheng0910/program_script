# encoding:utf-8

"""
获取主机所在网络的本地dns递归服务器地址
pip install dnspython
"""

import dns
import dns.resolver

def get_local_dns():
    default = dns.resolver.get_default_resolver()  # 获取默认解析器
    return default.nameservers  # 获取默认本地递归服务器地址
    # dns.resolver.default_resolver.nameservers = ['198.41.0.4']  # 设置本地递归服务器地址


if __name__ == '__main__':
    print get_local_dns()