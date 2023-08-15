import subprocess

# Run commands and capture their output
op_ip = subprocess.check_output("hostname -I | awk '{print $1}'", shell=True, text=True).strip()
business_ip = subprocess.check_output("hostname -I | awk '{print $2}'", shell=True, text=True).strip()
os_info = subprocess.check_output("lsb_release -ds", shell=True, text=True).strip().replace(',', ' ').replace('\n', ' ')
cpu_model = subprocess.check_output("lscpu | grep 'Model name' | cut -d: -f2", shell=True, text=True).strip().replace(',', ' ').replace('\n', ' ')
cpu_count = subprocess.check_output("lscpu | grep 'CPU(s):' | awk '{print $2}'", shell=True, text=True).strip()
cpu_frequency = subprocess.check_output("lscpu | grep 'CPU MHz' | cut -d: -f2", shell=True, text=True).strip()
memory_size = subprocess.check_output("free -h | grep 'Mem:' | awk '{print $2}'", shell=True, text=True).strip()
nvme_count = subprocess.check_output("lsblk | grep 'nvme' | wc -l", shell=True, text=True).strip()
nvme_block_size = subprocess.check_output("lsblk -b -d -o NAME,PHY-SEC | grep 'nvme' | awk '{print $2}'", shell=True, text=True).strip()
ssd_count = subprocess.check_output("lsblk | grep 'ssd' | wc -l", shell=True, text=True).strip()
ssd_block_size = subprocess.check_output("lsblk -b -d -o NAME,PHY-SEC | grep 'ssd' | awk '{print $2}'", shell=True, text=True).strip()
total_disk_size = subprocess.check_output("lsblk -b -d -o SIZE | awk '{s+=$1} END {print s}'", shell=True, text=True).strip()
network_info = subprocess.check_output("lshw -class network | grep 'product' | awk -F'product: ' '{print $2}'", shell=True, text=True).strip().replace(',', ' ').replace('\n', ' ')
kernel_version = subprocess.check_output("uname -r", shell=True, text=True).strip()

# Combine all outputs into a single line separated by commas
combined_output = ','.join([
    op_ip, business_ip, os_info, cpu_model, cpu_count, cpu_frequency, memory_size,
    nvme_count, nvme_block_size, ssd_count, ssd_block_size, total_disk_size,
    network_info, kernel_version
])

# Define the output file name
output_file = "system_info.csv"

# Write the combined output to the file as a single line
with open(output_file, "w") as f:
    f.write(combined_output + '\n')

print(f"Data saved to {output_file}")
