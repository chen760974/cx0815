import configparser
import base64
import codecs

def decode_credentials(encoded_credentials):
    # 对Base64编码的字符串进行解码
    decoded_credentials = base64.b64decode(encoded_credentials.encode('utf-8')).decode('utf-8')
    # 将解码后的字符串拆分成用户名和密码
    username, password = decoded_credentials.split(':')
    return username, password

def read_config(filename):
    config = configparser.ConfigParser()
    

    with codecs.open(filename, 'r', encoding='utf-8') as f:
        config.read_file(f)

    config.read(filename)

    server_info = {}
    for section in config.sections():
        if section.startswith('ServerIP_Group'):
            server_info[section] = {
                # 'Username': base64.b64decode(config.get(section, 'Username&&Passwd').encode('utf-8')).decode('utf-8'),
                # 'Password': base64.b64decode(config.get(section, 'Username&&Passwd').encode('utf-8')).decode('utf-8'),
                #'Username','Password':decode_credentials(config.get(section, 'Username&&Passwd')),
                'Username': config.get(section,'Username'),
                'Password': config.get(section,'Passwd'),
                'IPs': [config.get(section, key) for key in config.options(section) if key.startswith('ip')]
            }

    create_users = config.get('Create_Users', 'test_1').split('\n')
    
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
