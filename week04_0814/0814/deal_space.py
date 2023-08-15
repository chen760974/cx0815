import subprocess

# Run commands and capture their output
uname_output = subprocess.check_output("uname -a", shell=True, text=True).strip().replace(',', ' ').replace('\n', ' ')
lscpu_output = subprocess.check_output("lscpu", shell=True, text=True).strip().replace(',', ' ').replace('\n', ' ')
free_output = subprocess.check_output("free -h", shell=True, text=True).strip().replace(',', ' ').replace('\n', ' ')
df_output = subprocess.check_output("df -h", shell=True, text=True).strip().replace(',', ' ').replace('\n', ' ')
ifconfig_output = subprocess.check_output("ifconfig", shell=True, text=True).strip().replace(',', ' ').replace('\n', ' ')
os_release_output = subprocess.check_output("cat /etc/os-release", shell=True, text=True).strip().replace(',', ' ').replace('\n', ' ')

# Define the output file name
output_file = "system_info1.csv"

# Combine all outputs into a single line
combined_output = ','.join([
    " "," ",uname_output, lscpu_output, free_output, df_output, ifconfig_output, os_release_output
])

# Write the combined output to the file
with open(output_file, "w") as f:
    f.write(combined_output + '\n')

print(f"Data saved to {output_file}")
