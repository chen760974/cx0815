# 需要扩展功能：读服务器的配置文件
# server_info.items()是什么
# for group, info in server_info.items():看不懂
import configparser
import paramiko
import base64

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    server_info = {}
    for section in config.sections():
        if section.startswith('ServerIP_Group'):
            username = config.get(section, 'Username')
            password = config.get(section, 'Passwd')
            # 存在config文件里的密码是base64编码过的
            # password = base64.b64decode(password.encode()).decode()
            ips = [config.get(section, key) for key in config.options(section) if key.startswith('ip')]
            server_info[section] = {'Username': username, 'Password': password, 'IPs': ips}

    # create_users = [config.get('Create_Users', user) for user in config.options('Create_Users')]

    return server_info
    # 两个返回值server_info, create_users

if __name__ == "__main__":
    config_file = "config.ini"
    server_info = read_config(config_file)

    for group, info in server_info.items():
        # 分几组是应该的，同组的密码是一样的
        print(f"Group: {group}")
        print(f"Username: {info['Username']}")
        print(f"Password: {info['Password']}")


        print(f"Group: {group}, Username: {info['Username']}信息读取完成，存在当前目录{config_file}中")
        
        # print("IPs:")
        # for ip in info['IPs']:
        #     print(ip)
        # print()
        ##############

    # print("Create Users:")
    # for user in create_users:
    #     print(user)