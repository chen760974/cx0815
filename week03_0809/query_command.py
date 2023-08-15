import paramiko

def get_server_info(server_ip, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, username=username, password=password)

        # 通过SSH连接执行命令获取服务器信息
        command = "uname -a && lscpu && free -h && df -h && ifconfig && cat /etc/os-release"
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read().decode('utf-8')

        # 解析命令输出并提取所需信息
        # 这里需要根据实际输出进行解析，示例中仅提供了一个简单的示例
        # 你可能需要使用正则表达式或其他方法进行更准确的解析
        server_info = {
            '操作系统': 'Linux',
            'CPU型号': 'Intel Xeon',
            'CPU个数': 2,
            # ... 提取其他信息
        }

        ssh.close()
        return server_info
    except Exception as e:
        print("Error:", e)
        return None

# 设置服务器IP、用户名和密码
server_ip = 'your_server_ip'
username = 'your_username'
password = 'your_password'

# 获取服务器信息
info = get_server_info(server_ip, username, password)
if info:
    print(info)
else:
    print("Failed to retrieve server information.")
