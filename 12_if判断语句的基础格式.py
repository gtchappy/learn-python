"""
演示python判断语句：if语句的基本格式应用
"""
age = 30
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")

print("时间过得真快呀")

"""
演示练习题:成年人判断
"""
#
# 获取键盘输入
# age = int(input("请输入你的年龄:"))
#
# 通过if判断是否是成年人
# if age >= 18:
#     print("你已是成年人,游玩需要买票,10元")
# else:
#     print("你未成年,可以免费游玩")
# print("祝你游玩愉快")

"""
if else 练习题,我要买票吗
"""

# 定义键盘输入获取身高数据
height = int(input("请输入你的身高"))

# 通过if进行判断
if height > 120:
    print("你的身高超过120,需要买票,10元")
else:
    print("你的身高小于120,可以免费游玩")
print("祝你游玩愉快")
