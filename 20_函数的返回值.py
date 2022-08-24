"""
函数的返回值
"""


#
# def add(x, y):
#     result = x + y
#     return result
#
#
# num = add(1, 2)
# print(num)

"""
无return语句的函数返回值
"""
# def say_hi():
#     print("你好呀")
#
#
# result = say_hi()
# print(f"无返回值函数,返回的内容是:{result}")
# print(f"无返回值函数,返回的内容类型是:{type(result)}")
"""
主动返回None函数
"""
# def say_hi():
#     print("你好呀")
#     return None
#
#
# result = say_hi()
# print(f"无返回值函数,返回的内容是:{result}")
# print(f"无返回值函数,返回的内容类型是:{type(result)}")

# 用在if判断上
# 在if判断中,None等同于False

"""
None用于if判断
"""
# def check_age(age):
#     if age > 18:
#         return "success"
#     else:
#         return None
#
#
# result = check_age(16)
# # 如果返回值为空
# if not result:
#     print("未成年人禁止进入网吧")

"""
None用于声明无初试内容的变量
"""
# name = None
