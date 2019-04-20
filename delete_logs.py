# encoding:utf-8
"""
功能：清除程序运行生成日志(满足文件大小时，默认为50M，单位为M),支持系统为Ubuntu
author: mrcheng
适用场景：
长期在后台运行的探测程序，需要进行循环探测，期间会产生程序执行日志。
使用方法：
只要放在主函数里就行，每次遍历时执行。
"""

import os, commands


def get_file_size(file_path):
    """获取文件的大小（M）"""
    file_path = unicode(file_path, 'utf8')
    file_size = os.path.getsize(file_path)
    file_size = file_size/float(1024*1024)
    return int(file_size)


def delete_logs(file_path, file_size_threshold=50):
    """清除超过阈值的日志文件，阈值大小默认为50M"""
    exist = os.path.exists(file_path)
    if not exist:
        print "日志文件不存在，日志自动清理功能不执行，但探测程序正常运行"
        return
    file_name = file_path.split('/')[-1]
    file_size = get_file_size(file_path)
    if file_size >= file_size_threshold:    # 超过50M 后清除
        backup_command = 'cp ' + file_name + ' '+'backup_'+ file_name  # 备份命令
        commands.getstatusoutput(backup_command)  # 备份
        null_command = 'cat /dev/null > ' + file_name  # 清空命令
        commands.getstatusoutput(null_command)  # 清理