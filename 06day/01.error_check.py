# print(1/0)
#
# print('go on ... ?')

# try:(被捕获异常的代码) ->
# except:(在expect中来处理try代码块中产生的异常) ->
# finally:()

try:
    print(1/0)
    print(a + b)
except ZeroDivisionError as error:
    print("ZeroDivisionError: 在文件中的print(1/0)位置0不能作为除数!.{}".format(error))
except NameError as error:
    print("NameError: 在文件中不能存在print(未定义的变量).{}".format(error))

print('go on ... ?')


try:
    print(1/0)
except Exception as error:
    print("Error: except's Exception info: {}".format(error))

print('go on ... ?')


try:
    print(1/0)
except:
    print('system error')

print('go on .. ?')


def add(a, b):
    try:
        return a / b
    except Exception as error:
        print(error)
    finally:
        print('finally is go on ...')


add(1, 0)


# 有必要么?
try:
    dict01 = {1: 1, 2: 2, 3: 3}
except Exception as error:
    print('字典声明错误.{}')
finally:
    print('end')
