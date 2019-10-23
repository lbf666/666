# 集合的声明方式, 集合的去重功能, 集合的基本方法, 集合之间的交并集, 成员判断

# 集合的声明方式
setA = {1, 2, 3, 4, 1, 2, 3, 4}
listA = [1, 2, 3, 4, 1, 2, 3, 4]

print(setA)
print(listA)

# print(setA[0])
# print(listA[0])

# 对集合进行遍历?
for element in setA:
    print(element)

# 集合的交集并集
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
# print(setA & setB)
# print(setA | setB)
# print(setA + setB)
# print(setA * 2)

# 集合中常用的基本方法
setA.pop()
print(setA)

setA.remove(3)
print(setA)

setA.add(1234)
print(setA)
setA.add(321)
print(setA)
setA.add(123)
print(setA)

# 成员关系判断
listA = [1, 2, 3.14, 'string', True]
for element in listA:
    if type(element) in {int, float}:
        print(element)

