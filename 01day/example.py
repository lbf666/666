
# 单个变量的赋值
# bianliangdemingzi = 1

# 多个变量的赋值
# n1, n2, n3 = 1, 2, 3

# 链式赋值
# v1 = v2 = v3 = 1

# 从用户的输入来获取变量的值
# read -p "please input: " var -->> ^[[:space:]]+$ -->> 匹配空白行
# var = input("please input: ")

# print(bianliangdemingzi)
# print(n1, n2, n3, v1, v2, v3)
# print()  # -->> 空行 -->> ^$

# 思考题:
# 1. 请书写一个程序, 来把人民币换算成美元. 最后的输出要求有"多少人民币换算成了多少美元";
# 要求由用户输入相应的人民币数值, 再由程序进行处理, 并打印出结果?
# rmb = float(input("please input rmb: "))
# rate = 0.1414
# dollar = rmb * rate
# print(rmb, "人民币转换成:", dollar, "美元")

# 练习题:
# 1. 写一个程序判断用户输入的是不是数字, 如果是那么是否是奇数?
number = input("please input number: ")
print(number.isdigit())
# if number.isdigit():
#     print("number not numbers")
# else:
#     print("number is numbers")

# 2. 写一个程序来计算用户输入数字的立方, 若输入的不是数字则提示其重新输入

# 3. 写一个程序来计算人民币转化为欧元, 若输入的不是数字则提示其错误

# 4. 根据输入的成绩进行打分, 学习成绩>=90分的同学用A表示;60-89分之间的用B表示;60分以下的用C表示;
n = int(input("please : "))
if n >= 90:
    print("A")
elif n >= 60 and n <= 89:
    print("B")
else:
    print("C")

# 5. 写一个程序判断用户输入的内容是否为空, 若为空则直接提示用户重新输入, 若不为空则打印用户输入
m = input("please: ")
if bool(m):
    print(m)
else:
    print("你输错了, 再来一次")
