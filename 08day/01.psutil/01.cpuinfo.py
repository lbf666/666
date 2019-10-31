import psutil

# logical=True/False[True:逻辑核心数;False:物理核心数;]
print('CPU的核心数为: {}'.format(psutil.cpu_count(logical=True)))

# interval=[(values > 0.0):间隔起始和间隔结束的cpu时间进行比较;(percpu=True):对每个cpu进行单独统计]
print('CPU的整体占用情况: {}'.format(psutil.cpu_percent(interval=1, percpu=False)))
print('CPU的单核占用情况: {}'.format(psutil.cpu_percent(interval=1, percpu=True)))

# percpu=True/False[True:每个cpu的时间占用时间情况;False:整体cpu的时间占用时间情况]
print('CPU的整体占用情况: {}'.format(psutil.cpu_times(percpu=False)))
print('CPU的单核占用情况: {}'.format(psutil.cpu_times(percpu=True)))

# interval=[(values > 0.0):间隔起始和间隔结束的cpu时间进行比较;(percpu=True):对每个cpu进行单独统计]
print('CPU的整体各部分占比情况: {}'.format(psutil.cpu_times_percent(interval=1, percpu=False)))
print('CPU的单核各部分占比情况: {}'.format(psutil.cpu_times_percent(interval=1, percpu=True)))

cpuinfo = psutil.cpu_times_percent(interval=2)
print(cpuinfo.user)
print(cpuinfo.system)
print(cpuinfo.idle)

