"""
此脚本是在本计算机上查询各信息，存在.csv文件中
"""

import subprocess

# Define the output file name
output_file = "system_info5.csv"

# Column headers
headers = [
    "op网ip", "业务网ip", "操作系统", "CPU型号", "CPU个数", "CPU主频", 
    "内存大小", "nvme数量", "nvme单块大小", "SSD数量", "SSD单块大小", 
    "总硬盘大小", "网卡型号和数量", "内核版本", "操作系统"
]

# Run commands and capture their output
op_ip = "YOUR_OP_IP"  # Replace with actual OP IP
business_ip = "YOUR_BUSINESS_IP"  # Replace with actual Business IP
os_info = subprocess.check_output("cat /etc/os-release | grep PRETTY_NAME | cut -d '=' -f 2", shell=True, text=True).strip().replace(',', ' ')
cpu_info = subprocess.check_output("lscpu | grep 'Model name' | cut -d ':' -f 2", shell=True, text=True).strip().replace(',', ' ')
cpu_count = subprocess.check_output("lscpu | grep 'CPU(s)' | grep -v NUMA | grep -v list | cut -d ':' -f 2", shell=True, text=True).strip().replace(',', ' ')
cpu_frequency = subprocess.check_output("lscpu | grep 'CPU MHz' | cut -d ':' -f 2", shell=True, text=True).strip().replace(',', ' ')
memory_info = subprocess.check_output("free -h | grep 'Mem:' | awk '{print $2}'", shell=True, text=True).strip().replace(',', ' ')
# You can add similar commands for other information
nvme_count = subprocess.check_output("lsblk | grep 'nvme' | wc -l", shell=True, text=True).strip().replace(',', ' ')
nvme_block_size = subprocess.check_output("lsblk -b -d -o NAME,PHY-SEC | grep 'nvme' | awk '{print $2}'", shell=True, text=True).strip().replace(',', ' ')
ssd_count = subprocess.check_output("lsblk | grep 'ssd' | wc -l", shell=True, text=True).strip().replace(',', ' ')
ssd_block_size = subprocess.check_output("lsblk -b -d -o NAME,PHY-SEC | grep 'ssd' | awk '{print $2}'", shell=True, text=True).strip().replace(',', ' ')
total_disk_size = subprocess.check_output("lsblk -b -d -o SIZE | awk '{s+=$1} END {print s}'", shell=True, text=True).strip().replace(',', ' ')
network_info = subprocess.check_output("lshw -class network | grep 'product' | awk -F'product: ' '{print $2}'", shell=True, text=True).strip().replace(',', ' ')
kernel_version = subprocess.check_output("uname -r", shell=True, text=True).strip().replace(',', ' ')

# Combine all information into a single line separated by commas
machine_info = ','.join([
    op_ip, business_ip, os_info, cpu_info, cpu_count, cpu_frequency, memory_info, nvme_count, nvme_block_size, ssd_count, 
    ssd_block_size, total_disk_size, network_info, kernel_version
    # Add more information here in the same order as in the headers
])

# Write the headers to the file
with open(output_file, "w") as f:
    f.write(','.join(headers) + '\n')

# Append the machine information to the file as a single line
with open(output_file, "a") as f:
    f.write(machine_info + '\n')

print(f"Data saved to {output_file}")
