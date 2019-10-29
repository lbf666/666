# 装饰器: 利用闭包的概念,对传入的函数进行装饰
# 计算一个函数或某个功能执行的时间


# 实现加法的函数
def add(a, b):
    return a + b


# 装饰函数可以使用方式一:
print('要执行了...')
print(add(1, 2))
print('执行完了...')

# 方式二: 装饰器
def waibu(function_name):
    def neibu(*args):
        print('要执行啦...')
        function_name(*args)
        print('执行完了...')
    return neibu


@waibu  # 语法糖
def add(a, b):
    print(a + b)


add(1, 2)

# 模拟用户登录过程
database = {'tom': '123456', 'tony': 'abcabc', 'jack': 'bbc123'}

def checkLoad(func):
    def wrapper(user, password):
        if user in database.keys():
            if password == database[user]:
                func(user, password)
            else:
                print('密码错误')
        else:
            print('去注册吧...')
    return wrapper


@checkLoad
def load(user, password):
    print("Download......")


load('tom', '123456')
