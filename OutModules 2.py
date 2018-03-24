import requests

r = requests.get('http://www.sustc.edu.cn/')
print(r.status_code)
# print(r.text)
print(r.encoding)

import chardet

print(chardet.detect(b'Hello World!'))
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

import psutil

# 获取CPU信息
print('\n获取CPU信息')
print(psutil.cpu_count())

print(psutil.cpu_count(logical=False))

print(psutil.cpu_times())

for x in range(5):
    print(psutil.cpu_percent(interval=1,percpu=True))

# 获取内存信息
print('\n获取内存信息')
print(psutil.virtual_memory())
print(psutil.swap_memory())

# 获取磁盘信息
print('\n获取磁盘信息')
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))

# 获取网络信息
print('\n获取网络信息')
print(psutil.net_io_counters())
print(psutil.net_if_addrs())

# 获取进程信息
print('\n获取进程信息')
print(psutil.pids())

