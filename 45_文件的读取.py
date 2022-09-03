"""
演示对文件的读取
"""
import time

# 打开文件
f = open("C:/Users/gtc/Desktop/test.txt", "r", encoding="UTF-8")
print(type(f))

# 读取文件 - read()
# print(f"读取十个字节的结果：{f.read(10)}")
# print(f"read方法读取全部内容的结果是：{f.read()}")

# 读取文件 - readlines()
# lines = f.readlines()
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容是：{lines}")

# 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")

# for 循环读取文件行
# for line in f:
#     print(f"每一行的数据时：{line}")

# 文件的关闭
# f.close()

# with open 语法操作文件(该语法可以在执行完后自动关闭文件)
for line in f:
    print(f"每一行的数据是：{line}")
