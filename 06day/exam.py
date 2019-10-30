# 1. 把分析日志的IP排名分析;状态码分析;访问资源分析;实现自定义模块化(造轮子);
# 2. 写一个用来排名的函数, 字典或列表或元组都可以排序, 不限方法;
def sorts(types):
    if type(types) in (list, tuple, dict):
        if isinstance(types, (list, tuple)):
            types = list(types)
            types.sort()
            return types
        else:
            types = dict(sorted(types.items(), key=lambda x: x[1], reverse=True))
            return types
    else:
        return 'error: {}'.format('输入错误.')

# 3. 使用递归函数实现, 求10-9+8-7+6-5+4-3+2-1结果;;
def add(n):
    if n == 0:
        return n
    return n * (-1)**n + add(n - 1)

# 4. 写一个用来检查用户登录的装饰器
users = {'tom': '123456', 'rose': '123456', 'jones': '567890'}
def load(func):
    def wrapper(user, password):
        if user in users.keys():
            if password == users[user]:
                func(user, password)
            else:
                return 'password error;'
        else:
            return '快去注册吧.'
    return wrapper

@load
def loadweb(user, password):
    print('download......')


loadweb('tom', '123456')

# 5. 过滤出['string', 23, True, 13, 2.14, 3.1532, "tuple", [1, 2, 3, 4]]所有的数字
listA = ['string', 23, True, 13, 2.14, 3.1532, "tuple", [1, 2, 3, 4]]
listB = []
for element in listA:
    if not type(element) == bool:
        if isinstance(element, (int, float)):
            listB.append(element)
        elif isinstance(element, (tuple, list)):
            for e in element:
                listB.append(e)
print(listB)

# 6. 求[1, 2, 3.89, 4, 5.23, 6, 3.14, 5.98]所有元素相加后的结果;
from functools import reduce

listC = [1, 2, 3.89, 4, 5.23, 6, 3.14, 5.98]
print('result = {:.2f}'.format(reduce(lambda a, b: a + b, listC)))



