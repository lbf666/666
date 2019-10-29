# 函数可以赋值给一个变量
def add(a=0, b=0):
    return a + b


result = add
print(result(1, 2))

# 匿名函数: lambda variable: expression
# y = ax + b -> ax + b - y = 0
adds = lambda x, y: 3*x + y + 10
print(adds(3, 4))



