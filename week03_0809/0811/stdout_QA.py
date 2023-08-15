import paramiko

def execute_ssh_command(server_ip, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, username=username, password=password)

        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode('utf-8')

        ssh.close()

        return output
    except Exception as e:
        print("Error:", e)
        return None

# 设置服务器IP、用户名和密码
server_ip = 'your_server_ip'
username = 'your_username'
password = 'your_password'

# 要执行的命令
command = "lscpu && free -h && df -h && ifconfig && cat /etc/os-release"

# 执行命令并获取输出
output = execute_ssh_command(server_ip, username, password, command)
if output:
    print(output)
else:
    print("Failed to execute the command.")
