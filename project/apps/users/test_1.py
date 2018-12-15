#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import socket
import platform
from subprocess import Popen, PIPE, STDOUT
import json

# 得到主机名
def host_name():
    system = os.name
    if system == 'nt':
        return os.getenv('computername')
    elif system == 'posix':
        host = os.popen('hostname') # ('echo $HOSTNAME') # # 方法是os.popen(命令,权限,缓冲大小),该方法不但执行命令还返回执行后的信息对象
        try:
            print(host.read(), 'try')
            return host.read()
        finally:
            host.close()
        # hostname = Popen(["hostname"], stdout=PIPE)
        # return hostname.stdout.read()
    else:
        raise RuntimeError('Unkwon hostname')


#主机名相同则为开发环境，不同则为部署环境
#ALLOWED_HOSTS只在调试环境中才能为空
if socket.gethostname().lower() == host_name().lower():
    DEBUG = True
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = [
        'p.com',
        '0.0.0.0'
    ]
    DEBUG = False

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
print(host_name, ip) # ubuntu 127.0.1.1
print(DEBUG, ALLOWED_HOSTS) # False ['p.com', '0.0.0.0']

myname = socket.getfqdn(socket.gethostname())
print(myname) #ubuntu

platform = platform.system()
print(platform) # Linux

cwd = os.getcwd()
base_dir = os.path.basename(cwd)
print(base_dir) # users

home_dir = os.path.expanduser('~')
print(home_dir) #/home/xmzd

''' 获取Linux系统主机名称 '''
# def getHostname():
#     with open('/etc/sysconfig/network') as fd:
#         for line in fd:
#             if line.startswith('HOSTNAME'):
#                 hostname = line.split('=')[1].strip()
#                 break
#     return {'hostname':hostname}
#
# print(getHostname())

''' 获取Linux系统的版本信息 '''
def getOsVersion():
    with open('/etc/issue') as fd:
        for line in fd:
            osver = line.strip()
            break
    return {'osver':osver}

print(getOsVersion()) # {'osver': 'Ubuntu 18.04.1 LTS \\n \\l'}

#获取主机名,也可以使用 uname -n 命令获取
def hostname():
    hostname = Popen(["hostname"], stdout=PIPE)
    hostname = hostname.stdout.read()
    return hostname
hn = hostname()
print(str(hn))

# b = os.popen('ls')
# print(b.read())

# 方法是os.popen(命令,权限,缓冲大小),该方法不但执行命令还返回执行后的信息对象
test_host = os.popen('echo $HOSTNAME', 'r')
print(test_host.read(), '0000000000')

hostname = Popen(["hostname"], stdout=PIPE, stderr=STDOUT)
hostname = hostname.stdout.read()
print(hostname, '03165132')

h = os.popen('hostname')
print(h.read())