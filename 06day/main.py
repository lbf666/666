from logAnalysis.ips import ipAnalysis
# 从哪个子包(路径)中,导入哪个模块

ips = ipAnalysis.ipAnalysis('03day/access_log')
print(ips)

