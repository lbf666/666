import psutil
import json
import time


# user / system + stop / io / idle
# 所有进程占用cpu的时间
cpu = psutil.cpu_times()
print(cpu)

# 检测CPU被各个进程占用的时间百分比
# cpuInfo = psutil.cpu_times_percent(interval=1)
# print('user process percent: {}%'.format(cpuInfo.user))
# print('system process percent: {}%'.format(cpuInfo.system))
# print('iowait process percent: {}%'.format(cpuInfo.iowait))
# print('idle process percent: {}%'.format(cpuInfo.idle))

# 后端生产数据([python]Django) -->> (VUE/React[JavaScript]-[json])前端消费数据: 显示到页面中(给用户(运维)看)
# [{20190820162004: {user: None, system: None, iowait: None, idle: None}}]


def data():
    cpuInfo = psutil.cpu_times_percent(interval=1)
    date = time.strftime('%Y%m%d%H%M%S', time.localtime())
    module = [{date: {'user': cpuInfo.user, 'system': cpuInfo.system, 'iowait': cpuInfo.iowait, 'idle': cpuInfo.idle}}]
    return module


source = []
for bout in range(10):
    source.extend(data())
result = json.dumps(source)
print(result)
print(type(result))

