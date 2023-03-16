import configparser

# 创建一个配置文件
config = configparser.ConfigParser()

# 添加数据到配置文件
config.add_section('database')
config.set('database', 'openai_api_key', '')
config.set('database', 'port', '5432')
config.set('database', 'user', 'postgres')
config.set('database', 'password', 'mypassword')

config.add_section('debug')
config.set('debug', 'log_errors', 'true')
config.set('debug', 'show_warnings', 'true')

# 保存配置文件
with open('config.ini', 'w') as f:
    config.write(f)
# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 获取配置文件中的值
host = config.get('database', 'host')
port = config.get('database', 'port')
user = config.get('database', 'user')
password = config.get('database', 'password')
log_errors = config.getboolean('debug', 'log_errors')
show_warnings = config.getboolean('debug', 'show_warnings')

print(f"Database host: {host}")
print(f"Database port: {port}")
print(f"Database user: {user}")
print(f"Database password: {password}")
print(f"Log errors: {log_errors}")
print(f"Show warnings: {show_warnings}")


# config.set('openai_api_key', '')
# with open('config.ini', 'w') as f:
#     config.write(f)
# # 读取配置文件
# config = configparser.ConfigParser()
# config.read('config.ini')