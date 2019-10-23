# 元组的声明方法, 元组与列表的比较, 元组的遍历, 元组的切片, 元组的基本方法

# 元组的声明
tupleA = (1, 2, 3, 'string', True, 3.14, 1, 2, 3, 4)
listA = [1, 2, 3, 'string', True, 3.14, 1, 2, 3, 4]

# 元组的特点是: 不支持修改(元组是固定的), 元组所占用的内存空间比列表要小
tupleB = tupleA + (1, 2, 3)
print(tupleB)

# tupleA叫做变量的名字: 代表的是一段内存空间
# tupleA = tupleA + (1, 2, 3)时, 在赋值符号的右边的tupleA是去调用内存中所存在的元组,
# 赋值符号的左边tupleA是指向了, 由(1, 2, 3, 'string', True, 3.14)与(1, 2, 3)所占空间进行了
# 合并的操作, 并不是对元组本身进行了修改或增加, 是内存与内存之间的一个合并

# 查看所占内存空间大小的魔术方法: __sizeof__()
print(tupleA.__sizeof__())
print(listA.__sizeof__())
#  72-88 -> +16(88)-+16(104) -> +16(104)-+16(120)

# 遍历元组
for index in range(len(tupleA)):
    print(tupleA[index])

for element in tupleA:
    print(element)

# 元组的切片
print(tupleA[0:3])
# error: str + int
# print(' '.join(listA[::-1]))
# print('str0001' + 1)

# 元组的基本方法
n = tupleA.index('string', 0, len(tupleA) - 1)
print(n)
m = tupleA.count(1)
print(m)

# isinstance(variable, (str, int))
# if type(variable) in (str, int, float):
