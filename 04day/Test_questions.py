# 使用while循环, 反转句子"hello Tony, this my sister"; 反转后为"sister my this, Tony hello";
sentence = "hello Tony, this my sister"
# print(' '.join(sentence.split()[::-1]))
sentence_list = sentence.split()
sentence_list.reverse()
sentence_result = ''
for element in sentence_list:
    sentence_result += element + ' '
print(sentence_result.strip())

# 列表["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]转换成["string", "tuple", "list", 1, 2, 3, 4, 5, 6, 7];
listA = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
listB = []
for element in listA:
    if isinstance(element, (int, float, str, bool)):
        listB.append(element)
    else:
        for e in element:
            listB.append(e)
listA = listB
print(listA)

# 对[23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]进行排序;
# 方式一: sort
listC = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
listC.sort(reverse=True)
print(listC)
# 方式二: 冒泡
for i in range(len(listC)):
    for j in range(len(listC) - 1):
        if listC[j] < listC[j+1]:
            listC[j], listC[j+1] = listC[j+1], listC[j]
print(listC)

# 字符串"hello7723world45d78", 把其中的数字提取到一个元组中;
listD, string = [], "hello7723world45d78"
for element in string:
    if element.isdigit():
        listD.append(element)
print(tuple(listD))


# 利用函数求取10的阶乘结果;
def add(n=1):
    if n == 1:
        return n
    return n * add(n - 1)
print(add(10))


# 书写一个函数, 实现让用户输入验证码, 并判断用户输入的验证码正确与否;
import random
def checkCode(number=4):
    cc = []
    for i in range(number):
        cc.append(str(random.randint(0, 9)))
        cc.append(chr(random.randint(65, 90)))
    return ''.join(cc[:number])

while True:
    codes = checkCode(8)
    print('check code is : {}'.format(codes))
    user_input = input("input: ")
    if user_input.upper() == codes:
        print('load successfully')
        break
    else:
        print("验证码输入不正确, 请重新输入")

