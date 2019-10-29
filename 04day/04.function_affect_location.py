# 全局变量与局部变量


variable = '123'    # global variable


def sums():
    # print(variable)
    global variable
    variable = '456'
    print(variable)


sums()
print(variable)
