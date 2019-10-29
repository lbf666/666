# 高级函数: filter; reduce; map; sorted;
# 特点: 先传入一个具备相应功能的函数,再传入一个可被迭代的对象(list,string,tuple)

# map函数: 对可迭代对象中每一个元素进行操作
def findou(element):
    if element % 2 == 1:
        return element * 2
    else:
        return element

print((list(map(findou, [1, 2, 3, 4, 5]))))


listA = [1, 2, 3, 4, 5]
for index in range(len(listA)):
    if listA[index] % 2 == 1:
        listA[index] = listA[index] * 2
print(listA)


# filter函数: 对可迭代对象中符合条件的, 进行输出, 不符合的元素进行过滤
# 10000 *
def findrd(element):
    if element % 2 == 1:
        return element


print(list(filter(findrd, [1, 2, 3, 4, 5, 6, 7])))


# reduce函数: 把可迭代对象中所有的元素进行计算
# 计算方式为: 前两位计算结果与第三位再次进行相同的计算
from functools import reduce
def add(a, b):
    return a + b


print(reduce(add, (1, 2, 3, 4, 5, 6, 7, 8, 9)))

# sorted函数: 排序 100000 *
ips = {'1.1.1.1': 45, '2.2.2.2': 12, '3.3.3.3': 34, '4.4.4.4': 78}
# for i in ips.items():
#     print(i[1])
#
# def find(iterable):
#     for i in iterable:
#         print(i[1])
#
# for i in ips.items():
#     f = lambda element: element[1]
#     print(f(i))

print(dict(sorted(ips.items(), key=lambda x: x[1], reverse=True)[:2]))
print(ips.items())
# [('1.1.1.1', 45), ('2.2.2.2', 12), ('3.3.3.3', 34), ('4.4.4.4', 78)]
# sorted函数会自动的遍历列表^, 每个元素会被传送到key所代表的函数中;
# key= lambda x: x[1] -->> 找出 key = lambda ('1.1.1.1', 45): ('1.1.1.1', 45)[1]
# -->> key=45 -->> keys
# reverse=False/True
# 最后sorted函数会返回一个普通列表

