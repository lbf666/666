# 学习python中的变量
# filepath: cloud1906/01day/01.variable.py
# date: 2019/10/21 11:40
# modify_times: @pass
# author: liuchao


# python中如何声明变量
variable01 = 1
variable02 = 2
# 内存中开辟了一段空间, 赋予该空间一个地址, 把用户所规定的的变量名字等价于该内存的地址

# 多变量赋值方式
variable03, variable04 = 3, 4
variable05, variable06, variable07 = 5, 6, 7

# 链式赋值
variable08 = variable09 = 9

# shell: read -p "please input: " variable
variable = input("please input: ")

# python中打印变量的值 print
print("variable01的值为: ", variable01)
print(variable01, variable02, variable03, variable04)
