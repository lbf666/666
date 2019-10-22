# 列表: 声明方法, 如何遍历, 基本操作, 变量值交换, 算法(冒泡排序, 二分查找)
# 四种数据类型: int,float,str,bool叫做python中的基石;
# 四中数据结构: 元组(tuple), 列表(list), 字典(dict), 集合(set)

# 声明list的方式
listA = [18, 3.14, 'string', True]
print(listA, type(listA))
if isinstance(listA, list):
    print("yes")

listB = [x for x in range(1, 101) if x % 2 == 0]
print(listB)

# 对列表进行遍历
for index in range(len(listA)):
    print(listA[index])
print(listA[1])

for element in listA:
    print(element)

# 列表的加法
listC = [1, 2, 3, 4, True, False]
listD = [5, 6, 7, 'string']
print(listC + listD)

# 列表的乘法?
print(listC * 20)

# 列表的减法?
# listE = [1, 2, 3, 4]
# listF = 1
# print(listE - listF)

