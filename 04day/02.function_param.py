# 函数参数的演进过程
def println(a, b, c, d):
    print(a, b, c, d)


# println(1, 2, 3, 4, 5)

# python传入不定长参数
def printf(*args):
    for element in args:
        if isinstance(element, (int, float)):
            print(element)
        else:
            print("[Error] 该类型不是数字!")


printf('string', 123, 4.445, '123', True)
# printf(1, 2, 3, 4, 5, 6, 7, 8)

