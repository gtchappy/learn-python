# 方式1: 使用print直接输出类型信息
print(type("你好"))
print(type(123))
print(type(11.33))
# 方式2: 使用变量存储type()语句的结果
string_type = type("你好")
int_type = type(123)
float_type = type(11.34)
print(string_type)
print(int_type)
print(float_type)
# 方式3: 使用type()语句,查看变量中存储的数据类型信息
name = "你好"
name_type = type(name)
print(name_type)

