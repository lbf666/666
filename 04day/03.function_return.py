# 函数中的返回值, return
# print('hello world'.replace('o', 'O'))
# 'hello world'.replace('o', 'O')


def Sums(a=0, b=0):
    result = a + b
    return result


print(Sums(23, 45))
n = Sums(23, 45)
print(n)


# return是函数体结束的标志
def Sums01(a=0, b=0):
    if type(a) == int and type(b) == int:
        return a + b
    if isinstance(a, int) and isinstance(b, int):
        print('go on...')


print(Sums01(23, 45))


# return关键字的应用(递归算法)
sums = 0
for i in range(100000000):
    sums += i
print(sums)


def add(n=0):
    if n == 0:
        return n
    return n + add(n - 1)

# add(100) -> False -> return 100 + add(100 - 1)
#                             100 + -> 99 + add(99 - 1) -> 199 + add(98)
#


# print(add(998))
