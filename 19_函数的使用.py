"""
统计字符串的长度
"""


# 使用len()函数进行字符串长度统计
# name = "itheima"
# length = len(name)
# print(length)

# 不使用len()实现字符串统计功能
# name = "itheima"
# count = 0
# for x in name:
#     if x:
#         count += 1
# print(f"字符串{name}的长度是{count}")


# 使用函数来优化这个过程
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f"字符串{data}的长度是{count}")
#
#
# my_len("这里有6个字")


# 定义2数相加的函数,通过参数接收被计算的2个数字
# def add(x, y):
#     result = x + y
#     print(f"{x}+{y}的结果是{result}")
#
#
# # 调用函数,传入被计算的2个数字
# add(1, 2)


# 定义函数,接受一个参数传入(数字类型,表示体温)
# def temperature(x):
#     print("请出示72小时核算证明,并配合测量体温")
#     if x < 38:
#         print(f"体温{x}摄氏度,请进")
#     else:
#         print(f"体温{x}摄氏度,需要隔离")
#
#
# temperature(37)
