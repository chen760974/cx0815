#!/usr/bin/env python
# coding=utf-8
import subprocess
import os

# 检查当前用户是否为root，因为只有root用户可以创建其他用户
if not os.geteuid() == 0:# 检查当前用户是否为root
    print("This script must be run as root.")
    exit(1)
#if not条件判断，不满足后面的条件执行下面的语句
#exit(1): exit()函数用于退出脚本的执行，参数1表示退出时返回的状态码，
#通常非零状态码表示脚本执行失败。在这里，脚本以状态码1退出，这是一种指示错误或非正常执行的方式。

#with open()语句是一个上下文管理器，它会在代码块执行完毕后自动关闭文件，确保资源的正确释放。
with open('userlist.txt') as f:
    for username in f:
        username = username.strip()  # 去除行末的换行符
        try:
            # 创建用户
            subprocess.run(['useradd', '-m', username], check=True)
            print(f"User {username} created.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create user {username}: {e}")
# 注意：如果在Python 3.6之前的版本中使用，请使用subprocess.check_call()代替subprocess.run()。
