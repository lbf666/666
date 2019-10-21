# shell语言if条件判断的框架;
# if [ ${a} -gt 0 ];then
#   echo "exist"
# else
#   echo "not exist"
# fi


# python语言if条件判断框架;
var = 2
if var > 0:
    print("gt")
else:
    print("lt")

# y = |x|
x = float(input("please input number: "))
if x >= 0:
    y = x
    print(y)
else:
    y = -x
    print(y)

# 判断一个字符串是否为空?
string = "abc"
if bool(string):
    pass
else:
    print("string is none.")
# 优化后的程序
# if not bool(string):
# if not True:
# if False:
if not bool(string):
    print("string is none.")
else:
    print("string is not none.")

################################
# if 条件判断的多条件判断
# 验证一个数字是否是个偶数
var = 18
if var % 4 == 0:
    print("var is odd")
elif var % 3 == 0:
    print("var能被3整除")
elif var % 9 == 0:
    print("var能被9整除")
else:
    print("......")

# if 条件判断的嵌套
# 判断一个数, 是否能被2整除,也能被3整除
number = 12
if number % 2 == 0:
    if number % 3 == 0:
        print("yes")
    else:
        print("只能被2整除")
else:
    if number % 3 == 0:
        print("只能被3整除")
    else:
        print("既不能被2整除, 也不能被3整除")
# 优化代码:
if number % 2 == 0 and number % 3 == 0:
    print("yes")
elif number % 2 == 0:
    print("只能被2整除")
elif number % 3 == 0:
    print("只能被3整除")
else:
    print("no")

# 对于if条件判断而言: if可以单独使用, 但是elif以及else不能单独使用,必须与if成对儿出现
#
# 总结:
#   1. 对于多条件判断时使用if...elif...elif...else...框架
#   2. 对于多个条件需同时满足的情况使用:
#   if .. and .. :
#       pass
#   else:
#       pass
#   3. 对于一些出现错误的情况较多的输出程序: 使用的判断框架为
#   if not .. :
#       输出错误情况的提示或处理错误的动作
#   else:
#       输出正确情况的提示或后续的处理动作

