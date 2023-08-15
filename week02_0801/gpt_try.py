import configparser
import base64

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    server_info = {}
    for section in config.sections():
        if section.startswith('ServerIP_Group'):
            username = config.get(section, 'Username')
            password = config.get(section, 'Passwd')
            print(password)
            password = base64.b64decode(password.encode()).decode()
            ips = [config.get(section, key) for key in config.options(section) if key.startswith('ip')]
            server_info[section] = {'Username': username, 'Password': password, 'IPs': ips}

    create_users = [config.get('Create_Users', user) for user in config.options('Create_Users')]

    return server_info, create_users

if __name__ == "__main__":
    config_file = "config.ini"
    server_info, create_users = read_config(config_file)

    for group, info in server_info.items():
        print(f"Group: {group}")
        print(f"Username: {info['Username']}")
        print(f"Password: {info['Password']}")
        print("IPs:")
        for ip in info['IPs']:
            print(ip)
        print()

    print("Create Users:")
    for user in create_users:
        print(user)

    print("执行成功了呗")
