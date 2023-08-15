"""
还是gpt的工作内容
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
    # Define remote server details
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
            "op_ip", "business_ip", "os_info", "cpu_model", "cpu_count", "cpu_frequency",
            "memory_size", "nvme_count", "nvme_block_size", "ssd_count", "ssd_block_size",
            "total_disk_size", "network_info", "kernel_version"
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
