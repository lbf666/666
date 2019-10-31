# psutil: 提取物理内存的信息和虚拟内存的信息
import psutil


print(psutil.virtual_memory())
print(psutil.swap_memory())

print('*'*20)

print(psutil.disk_partitions())
diskinfo = psutil.disk_usage('/')

print(diskinfo.total)

