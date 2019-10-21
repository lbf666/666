# python中基本的数据类型都有: 整型(int), 浮点型(float), 字符串类型(str), 布尔值类型(bool)
# 整型(int): 0, 1, 2, 3, 4, ....
# 浮点型(float): 0.0, 3.14, 4.445 ... (浮点数的标记就是有小数点)
# 字符串类型(str): 以单引或双引或三引, 引起来的字符(数字, 字母, 特殊字符...), 我们就称它字符串类型;
# 布尔值类型(bool): True, False

# 整型数据的基本操作
n1, n2 = 12, 4
# 四则运算
print("n1 + n2 = ", n1+n2)
print("n1 - n2 = ", n1-n2)
print("n1 * n2 = ", n1*n2)
print("n1 / n2 = ", n1/n2)

# 取整, 取余, 取幂
print("n1对n2取整结果为: ", n1//n2)
print("n1对n2取余结果为: ", n1%n2)
print("取n1的二次幂: ", n1**2)

# 浮点型的基本操作
v1, v2 = 3.14, 100
print("v1 + v2 =", v1+v2)
print("v1 * v2 =", v1*v2)
print("v1 - v2 =", v1-v2)
print("v1 / v2 =", v1/v2)

# 取整, 取余, 取幂
print("v1对v2取整: ", v1//v2)
print("v1对v2取余: ", v1%v2)
print("对v1进行取二次幂: ", v1**2)


# 字符串类型的基本操作
s1, s2 = "hello", 'world'
# s3, s4 = '''''', """"""
s3 = "hello" \
     "world"
s4 = """hello
world"""
print(s3)
print(s4)

# 字符串的基本操作
print("s1 + s2 =", s1+' '+s2)
print("s1*20", s1*20)
s5 = "*"
print(s5*10 + '这是分割线' + s5*10)

# 布尔值类型
# and(全为真时为真) // or(都为假时为假,若有一方为真则为真) // not(对条件取反)
print(True and False)
print(True or False)
print(not False)





