# 读取文件以及写入文件的两种方式

# 读取文件的模式是mode='r'
file = open(file='/etc/passwd', mode='r') # vim /etc/passwd
# print(file.read())        # 输出整个文章的内容
# print(file.readline())
# print(file.readline())    # 生成器, 每次调用都会打印出一行
print(file.readlines())     # 输出一个把每一行作为元素的列表
file.close()    # :wq

# 写入内容到文件中,使用mode='w'
files = open(file='./fileIO.txt', mode='w') # vim /etc/passwd
files.write(            # mode='w'时, file.write()函数写如内容到文件时会进行覆盖操作
    """
# File IO Opera
- email: hlions@163.com
- author: hlions
    """
)
files.writelines('abcdefghijklmn')
files.writelines(['abc\n', 'bcd\n', 'jkl\n'])       # 传入一个可迭代对象, 可以一次性添加多行内容
files.writable()                # 会返回相应的bool值, 我们可以用来判断文件的写入权限
files.close()

# 想在文件中追加内容时, 可以使用mode='a'
filess = open(file='./fileIO.txt', mode='a') # vim /etc/passwd
filess.write(
    """
    abc
    def
    jkl
    """
)
filess.close()


# 联系文件上下文来打开文件, 并对文件进行相应的操作
with open(file='./with_file.txt', mode='a') as filesss:
    pass
