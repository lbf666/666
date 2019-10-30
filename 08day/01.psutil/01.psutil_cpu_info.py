# pip是在python中安装第三方库的命令, 类似于Linux中安装软件的yum,apt,dnf
# pip install softname 安装python的第三方库
# pip uninstall softname 卸载python的第三方库
# pip list  列出已经安装的第三方库
# pip install --upgrade pip # 升级pip命令

# 系统cpu信息提取
import psutil


cpu_info = psutil.cpu_times_percent(interval=5, percpu=True)
print(cpu_info)

cpu_info = psutil.cpu_times()
print(cpu_info)

cpu_info = psutil.cpu_percent(interval=5)
print(cpu_info)

cpu_info = psutil.cpu_count(logical=False)
print(cpu_info)

