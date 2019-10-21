
# 单个变量的赋值
bianliangdemingzi = 1

# 多个变量的赋值
n1, n2, n3 = 1, 2, 3

# 链式赋值
v1 = v2 = v3 = 1

# 从用户的输入来获取变量的值
# read -p "please input: " var -->> ^[[:space:]]+$ -->> 匹配空白行
# var = input("please input: ")

print(bianliangdemingzi)
print(n1, n2, n3, v1, v2, v3)
print()  # -->> 空行 -->> ^$

# 思考题:
# 1. 请书写一个程序, 来把人民币换算成美元. 最后的输出要求有"多少人民币换算成了多少美元";
# 要求由用户输入相应的人民币数值, 再由程序进行处理, 并打印出结果?
rmb = float(input("please input rmb: "))
rate = 0.1414
dollar = rmb * rate
print(rmb, "人民币转换成:", dollar, "美元")


