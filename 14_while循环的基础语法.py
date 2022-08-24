"""
演示while循环的基础应用
"""
# i = 0
# while i < 100:
#     print("小美我喜欢你")
#     i += 1

"""
通过while循环,计算从1累加到100的和
"""
# sum = 0
# i = 1
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)

"""
通过while实现猜随机数的功能
"""
# import random
#
# num = random.randint(1, 100)
# 定义一个变量,记录总共猜测了多少次
# count = 0
# 通过一个布尔类型的变量,做循环是否继续的标记
# flag = True
# while flag:
#     guess_num = int(input("请输入你猜测的数字:"))
#     count += 1
#     if guess_num == num:
#         print("恭喜你猜对了")
#         flag = False
#     else:
#         if guess_num > num:
#             print("你猜大了")
#         else:
#             print("你猜小了")
#
# print(f"你总共猜了{count}次")
"""
演示while循环的嵌套使用
"""

# 外层:表白100天的控制
# 内层:每天的表白都送10支玫瑰花的控制
#
# i = 1
# while i <= 100:
#     print(f"今天是第{i}天,准备表白")
#     # 内层循环的控制变量
#     j = 1
#     while j <= 10:
#         print(f"送给小美第{j}支玫瑰花")
#         j += 1
#     print("小美,我喜欢你")
#     i += 1
# print(f"坚持到第{i-1}天,表白成功")

"""
在print语句中,加上end=''即可输出不换行
\t 来模拟键盘按下tab键
"""
# 输出不换行
# print("hello", end='')
# print("world")
# # 模拟按下tab键
# print("Hello\tWorld")

"""
通过while循环,输出九九乘法表
"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j * i}\t", end='')
        j += 1
    print("")
    i += 1
