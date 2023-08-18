"""
还是gpt的工作内容
此方案目测是可行的
1.缺点还是不能读文本，需要修改
"""

import subprocess
import paramiko

def get_system_info(ssh_client):
    commands = [
        "hostname -I | awk '{print $1}'",
        "hostname -I | awk '{print $2}'",
        "lsb_release -ds",
        "lscpu | grep 'Model name' | cut -d: -f2",
        "lscpu | grep 'CPU(s):' | awk '{print $2}'",
        "lscpu | grep 'CPU MHz' | cut -d: -f2",
        "free -h | grep 'Mem:' | awk '{print $2}'",
        "lsblk | grep 'nvme' | wc -l",
        "lsblk -b -d -o NAME,PHY-SEC | grep 'nvme' | awk '{print $2}'",
        "lsblk | grep 'ssd' | wc -l",
        "lsblk -b -d -o NAME,PHY-SEC | grep 'ssd' | awk '{print $2}'",
        "lsblk -b -d -o SIZE | awk '{s+=$1} END {print s}'",
        "lshw -class network | grep 'product' | awk -F'product: ' '{print $2}'",
        "uname -r"
    ]

    system_info = []

    for command in commands:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode().strip().replace(',', ' ').replace('\n', ' ')
        system_info.append(output)

    return ','.join(system_info)

def main():
    # Define remote server details IP, ROOT, PASSWORD
    remote_servers = [
        {"hostname": "server1.example.com", "username": "username", "password": "password"},
        {"hostname": "server2.example.com", "username": "username", "password": "password"},
        {"hostname": "server3.example.com", "username": "username", "password": "password"}
    ]

    # Define the output file name
    output_file = "system_info.csv"

    # Open the output file for writing
    with open(output_file, "w") as f:
        # Write headers
        headers = [
            "op网ip", "业务网ip", "操作系统", "CPU型号", "CPU个数", "CPU主频", 
            "内存大小", "nvme数量", "nvme单块大小", "SSD数量", "SSD单块大小", 
            "总硬盘大小", "网卡型号和数量", "内核版本"
        ]
        f.write(','.join(headers) + '\n')

        # Connect to remote servers, retrieve and write system info
        for server in remote_servers:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(server["hostname"], username=server["username"], password=server["password"])

            system_info = get_system_info(ssh_client)
            f.write(system_info + '\n')

            ssh_client.close()

    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()
