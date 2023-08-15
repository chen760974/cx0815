#!/usr/bin/env python
# coding=utf-8
import subprocess

# 示例1：运行一个简单的命令
result = subprocess.run(["ls", "-l"])

# 示例2：运行一个复杂的命令，捕获输出并指定编码
result = subprocess.run("echo 'Hello, World!'", shell=True, capture_output=True, text=True)
print(result.stdout)

# 示例3：捕获标准错误输出并检查返回状态码
try:
    result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True, universal_newlines=True)
    print("Command execution succeeded.")
    print(f"stdout: {result.stdout}")
    print(f"stderr: {result.stderr}")
except subprocess.CalledProcessError as e:
    print(f"Command execution failed with error: {e}")
    print(f"stdout: {e.stdout}")
    print(f"stderr: {e.stderr}")
