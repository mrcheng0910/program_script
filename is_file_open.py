# encoding=utf-8
"""
判断文件是否处于打开状态（Linux）
"""
import os


def is_file_open(filename):
    # 执行lsof命令
    p = os.popen("lsof %s" % filename)
    # lsof找到打开的文件时有输出
    content = p.read()
    p.close()
    # 通过是否有输出，判断文件是否打开
    return bool(len(content))


if __name__ == '__main__':
    print is_file_open("root.zone")