import psutil
import json
import time


memInfo = psutil.virtual_memory()
print(memInfo.total)    # 1024 bit = 1024 Kbit = 1 MBit = ? GBit
print('{:.0f}'.format(memInfo.total/1024/1024))
print('{:.0f}'.format(memInfo.free/1024/1024))
print('{:.0f}'.format(memInfo.used/1024/1024))
print('{:.0f}'.format(memInfo.buffers/1024/1024))
print('{:.0f}'.format(memInfo.cached/1024/1024))

swapInfo = psutil.swap_memory()
print(swapInfo)

diskInfo = psutil.disk_partitions()
print(diskInfo)
diskInfo = psutil.disk_io_counters()
print(diskInfo)
diskInfo = psutil.disk_usage('/')
print(diskInfo.total, diskInfo.free, diskInfo.used)

# 生成CPU/Memory/Disk的信息模板
monitorInfo = [{'date': {
    'cpu': {'user': None, 'system': None, 'iowait': None, 'idle': None},
    'memory': {'total': None, 'used': None, 'free': None, 'buffer': None, 'Cached': None},
    'disk': {'total': None, 'used': None, 'free': None}
}}]



