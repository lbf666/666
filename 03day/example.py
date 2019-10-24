# 练习题:
# 1. 统计出access_log文件中排名前五的IP地址;
ips = {}
with open(file='access_log', mode='r') as log:
    for lines in log.readlines():
        # lines.split()[0]
        if not lines.split()[0] in ips.keys():
            ips.setdefault(lines.split()[0], 1)
        else:
            ips[lines.split()[0]] += 1
ips_list = []
for element in ips.items():
    ips_list.append(element)
for i in range(len(ips_list)):
    for j in range(len(ips_list) - 1):
        if ips_list[j][1] < ips_list[j+1][1]:
            ips_list[j], ips_list[j+1] = ips_list[j+1], ips_list[j]
print(dict(ips_list[:5]))

# 2. 根据access_log文件统计出网站的pv量及uv量;
with open(file='access_log', mode='r') as log:
    ip, lines = [], log.readlines()
    for line in lines:
        # lines.split()[0]
        ip.append(line.split()[0])
    print("uv is {}".format(len(set(ip))))
    print("pv is {}".format(len(lines)))

# with open(file='access_log', mode='r') as file:
#     ip = []
#     for line in file.readlines():
#         # lines.split()[0]
#         ip.append(line.split()[0])
#     print("uv is {}".format(len(set(ip))))
#     print("pv is {}".format(len(file.readlines())))


# 3. 根据access_log文件统计出200, 403, 404, 502, 503状态码分别出现过多少次;
code = {}
with open(file='access_log', mode='r') as log:
    for lines in log.readlines():
        if lines.split()[8] in ('200', '404', '403', '502', '503'):
            if not lines.split()[8] in code.keys():
                code.setdefault(lines.split()[8], 1)
            else:
                code[lines.split()[8]] += 1
print(code)


# 4. 对字典{'1.1.1.1': 45, '2.2.2.2': 23, '3.3.3.3': 78, '4.4.4.4': 120}根据值进行从大到小的排序;
# 5. [1, 1, 1, 2, 3, 4, 5, 6, 7, 1, 3, 2, 4, 5, 2, 4, 6]中有多少个相互不同的元素?
listA = [1, 2, 3, 4]
print(listA[10:])

# list特点: 动态可变的
# 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 16^14
# -10 -9 .......                          9

username = input("username: ")
password = input("password: ")
if username in ('yangge', 'shark') and password == '123':
    print("load successfully")
else:
    if username in ('yangge', 'shark') and not password == '123':
        for i in range(3):
            password = input("password: ")
            if password == '123':
                print('load successfully')
                break
    else:
        print("快去注册吧,没你这人")


# 2-3+4-5+6-7+8.....+50
n = 0
for number in range(2, 51):
    if number % 2 == 0:
        n += number
    else:
        n -= number
print(n)

# 郝式解法
sum = 0
i = 2
while i <= 50:
    sum += i * (-1)**i
    i += 1
print(sum)


listA = ['www', 'qfedu', 'com']
print('.'.join(listA))





