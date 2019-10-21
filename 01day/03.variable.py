# 数据类型的转换

int01, float01, str01, bool01 = 18, 3.64, "hello", True

# int -> float
int01_to_float = float(int01)
print(int01_to_float, type(int01_to_float))

# float -> int # 注意点: 浮点类型转换为整型时,无法进行四舍五入
float01_to_int = int(float01)
print(float01_to_int, type(float01_to_int))

# int或float -> str
int01_to_str = str(int01)
print(int01_to_str, type(int01_to_str))
float01_to_str = str(float01)
print(float01_to_str, type(float01_to_str))

# str -> int或float
# str01_to_int = int(str01)
# print(str01_to_int, type(str01_to_int))
s1, s2 = "18", "3.14"
s1_to_int = int(s1)
s2_to_int = int(float(s2))
print(s1_to_int, type(s1_to_int))
print(s2_to_int, type(s2_to_int))

# 布尔类型的转换
# bool -> int
# print("True to int type: ", True, int(True), type(int(True)))
bool01_to_int = int(bool01)
print(bool01_to_int, type(bool01_to_int))

bool02 = False
bool02_to_int = int(bool02)
print(bool02_to_int, type(bool02_to_int))

# int -> bool # 结论: 非零数转化为bool类型后为True, 只有0是False;
int02 = -3
int02_to_bool = bool(int02)
print(int02_to_bool, type(int02_to_bool))

# str或float -> bool
float01_to_bool = bool(float01)
print(float01_to_bool, type(float01_to_bool))

float02 = -3.14
float02_to_bool = bool(float02)
print(float02_to_bool, type(float02_to_bool))

float03 = 0.0
float03_to_bool = bool(float03)
print(float03_to_bool, type(float03_to_bool))

# str -> bool # 结论: 字符串为空时判断为False, 字符串非空时为True
str01_to_bool = bool(str01)
print(str01_to_bool, type(str01_to_bool))

str02 = ""
str02_to_bool = bool(str02)
print(str02_to_bool, type(str02_to_bool))

# 总结:
# 1. 查看变量的类型所使用的的函数为: type(variable_name)
# 2. 基本数据之间的转换所使用的函数为: int() // float() // str() // bool()
