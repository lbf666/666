# 闭包: 由外部函数返回内部函数的名字,功能为在全局中调用内部函数
# 闭包中修改外部函数的变量,在内部函数中 -> 变量作用域


# 我们现在实现一个功能, 叫做计算器, 这个计算呢, 实现对应数字的对应次方
# result = x ** 2
# result = x ** 3
# result = x ** y
def waibu(y=1):
    def neibu(x=0):
        return x ** y
    return neibu


result = waibu(2)
print(result(4))
print(result(5))





