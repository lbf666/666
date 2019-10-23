# 字典的声明方式, 字典的特点(key-value), 字典的遍历, 字典的基本方法
# () -> [] -> {}

# 字典的声明
sidamingji = {'桃花源记': '陶渊明', '岳阳楼记': '范仲淹', '西游记': '吴承恩'}
print(sidamingji, type(sidamingji))

ips = dict([((1, 2, 3), [20, 23, 24, 25]), ('1.1.1.1', 20), ('1.1.1.1', 35), ('3.3.3.3', 89)])
print(ips)

# 遍历字典
# 如何去遍历字典的值
for keys in ips:
    print(ips[keys])
for values in ips.values():
    print(values)
# 如何去遍历字典的键
for keys in ips.keys():
    print(keys)
# 如何去遍历整个的键值对儿
for items in ips.items():
    print(items)

# 字典中的key就是list中的索引, 但是字典中的key具备可自定义性;
# ips01 = {'0': 1, 1: 2, 2: 3, 3: 4, 4: 5}
# listB = [1, 2, 3, 4, 5]
# print(ips01['0'])



ips = {'1.1.1.1': 23, '2.2.2.2': 23, '3.3.3.3': 32}
# 字典中增加键值对的操作
ips['4.4.4.4'] = 45
print(ips)

ips.setdefault('5.5.5.5', 89)
print(ips)

# 字典中删除键值
ips.pop('1.1.1.1')
print(ips)

# ips.popitem()
# print(ips)
# ips.popitem()
# print(ips)

# 字典的更改 -> 更改键值对中的值
ips['2.2.2.2'] = 2323
print(ips)

for i in range(1, 101):
    ips['3.3.3.3'] += i
print(ips)

ips.update([('2.2.2.2', 23.45), ('3.3.3.3', 56)])
print(ips)

# 字典的查
print(ips['2.2.2.2'])
print(ips.get('2.2.2.2'))

ips01 = {}
print(ips01.fromkeys([x for x in range(100)]))

# 思考题:
# {'1.1.1.1': 12, '2.2.2.2': 5, '3.3.3.3': 78, '4.4.4.4': 34}
# 按照字典中每个键值对的值大小进行排序; 要求从大到小;
ips = {'1.1.1.1': 12, '2.2.2.2': 5, '3.3.3.3': 78, '4.4.4.4': 34}
print(ips.items())
ips_list = []
for items in ips.items():
    ips_list.append(items)
for i in range(len(ips_list)):
    for j in range(len(ips_list) - 1):
        if ips_list[j][1] < ips_list[j+1][1]:
            ips_list[j], ips_list[j+1] = ips_list[j+1], ips_list[j]
print(dict(ips_list))
