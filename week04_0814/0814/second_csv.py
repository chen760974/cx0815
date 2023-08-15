import subprocess

# Run commands and capture their output
uname_output = subprocess.check_output("uname -a", shell=True, text=True).strip().replace(',', '')
lscpu_output = subprocess.check_output("lscpu| grep 'Model name'", shell=True, text=True).strip().replace(',', '')
free_output = subprocess.check_output("free -h", shell=True, text=True).strip().replace(',', '')
df_output = subprocess.check_output("df -h", shell=True, text=True).strip().replace(',', '')
ifconfig_output = subprocess.check_output("ifconfig", shell=True, text=True).strip().replace(',', '')
os_release_output = subprocess.check_output("cat /etc/os-release", shell=True, text=True).strip().replace(',', '')

# Define the output file name
#output_file = "system_info3.csv"

# Combine all outputs into a single line
combined_output = ','.join([
    uname_output, lscpu_output, free_output, df_output, ifconfig_output, os_release_output
])

# Write the combined output to the file
with open("system_info3.csv", "w") as f:
    f.write(combined_output + '\n')

print(f"Data saved to system_info3.csv")
