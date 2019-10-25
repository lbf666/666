# 函数的声明
def Sum():
    print(1+2)


# # python中调用函数的方法
# Sum()

# 函数中传入参数
def Sum01(a, b):
    print(a+b)


# Sum01()

# 设定函数的参数初值
def Sum02(a=0, b=0):
    print(a+b)


Sum02()
Sum02(23, 45)


def logAnalysis(filepath):
    with open(file='{}/access_log'.format(filepath), mode='r') as log:
        ips = {}
        for lines in log.readlines():
            if not lines.split()[0] in ips.keys():
                ips.setdefault(lines.split()[0], 1)
            else:
                ips[lines.split()[0]] += 1
        ips_list = []
        for kv in ips.items():
            ips_list.append(kv)
        for i in range(len(ips_list)):
            for j in range(len(ips_list) - 1):
                if ips_list[j][1] < ips_list[j+1][1]:
                    ips_list[j], ips_list[j+1] = ips_list[j+1], ips_list[j]
        print(dict(ips_list[:10]))


logAnalysis(filepath='../03day')

