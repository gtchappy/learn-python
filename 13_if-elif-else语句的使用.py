# 通过if判断,可以使用多条件判断的语法
# 第一个条件就是if
# 条件是互斥的,前面一个满足后面的就不执行
#
# if int(input("请输入你的身高")) < 120:
#     print("身高小于120cm,可以免费")
# elif int(input("请输入你的身高等级(1-5):")) > 3:
#     print("vip级别大于3,可以免费")
# elif int(input("请告诉我今天几号")) == 1:
#     print("今天是1号免费日,可以免费")
# else:
#     print("不好意思,条件都没满足,需要买票")


"""
猜数字案例编写
"""
# 定义一个数字
# num = 5

# 通过键盘输入获取猜想的数字,通过多次if 和 elif 的组合进行猜想比较
# if int(input("请猜一个数字")) == num:
#     print("恭喜第一次猜对了")
# elif int(input("猜错了再猜一次")) == num:
#     print("猜对了")
# elif int(input("猜错了,再猜一次")) == num:
#     print("恭喜,最后一次机会你猜对了")
# else:
#     print("很抱歉,全猜错了")

"""
定义一个数字(1~10,随机产生),通过3次判断来猜出数字
"""

# 1.构建一个随机的数字变量
import random

num = random.randint(1, 10)
print(num)
guess_num = int(input("请输入你要猜测的数字:"))

# 2.通过if判断语句进行数字的猜测
if guess_num == num:
    print("恭喜,第一次就猜中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")









