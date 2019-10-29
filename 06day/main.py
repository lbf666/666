# from logAnalysis.ips import ipAnalysis
# # 从哪个子包(路径)中,导入哪个模块
#
# ips = ipAnalysis.ipAnalysis('03day/access_log')
# print(ips)


# 计步器的写法
def jbq(step):
    def add():
        nonlocal step
        step += 1
        return step
    return add


# print(step())   # 走第一步
# print(step())   # 走第二步
def bs(steps=0):
    step_result = jbq(steps)
    while True:
        bbb = step_result()
        if bbb == 100:
            print(bbb)
            break
    return bbb


# 第一次停止:
first = bs()
print(first)

def bs(steps=0):
    step_result = jbq(steps)
    while True:
        bbb = step_result()
        if bbb == 1000:
            print(bbb)
            break
        print(bbb)
    return bbb


# 第二次停止:
second = bs(first)



