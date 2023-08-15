import subprocess

# Run commands and capture their output
uname_output = subprocess.check_output("uname -a", shell=True, text=True)
lscpu_output = subprocess.check_output("lscpu", shell=True, text=True)
free_output = subprocess.check_output("free -h", shell=True, text=True)
df_output = subprocess.check_output("df -h", shell=True, text=True)
ifconfig_output = subprocess.check_output("ifconfig", shell=True, text=True)
os_release_output = subprocess.check_output("cat /etc/os-release", shell=True, text=True)

# Define the output file name
#output_file = "system_info.csv"

# Write command outputs to the file
with open("system_info2.csv", "w") as f:
    #f.write("Command Output\n")

    f.write("uname -a"+","+uname_output + "\n")
    # f.write(uname_output + "\n")

    f.write("lscpu"+","+lscpu_output + "\n")
    # f.write(lscpu_output + "\n")

    f.write("free -h"+","+free_output + "\n")
    # f.write(free_output + "\n")

    f.write("df -h"+","+df_output + "\n")
    # f.write(df_output + "\n")

    f.write("ifconfig"+","+ifconfig_output + "\n")
    # f.write(ifconfig_output + "\n")

    f.write("cat /etc/os-release"+","+os_release_output + "\n")
    # f.write(os_release_output + "\n")

print(f"Data saved to system_info1.csv")
