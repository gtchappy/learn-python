"""
演示循环语句的中断控制:break和continue
"""

# 演示循环中断语句 continue
# for i in range(1, 6):
#     print("语句1")
#     continue
#     print("语句2")

# 演示continue的嵌套应用
# for i in range(1, 6):
#     print("语句1")
#     for j in range(1, 6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")

# 演示循环中断语句 break
# for i in range(1, 101):
#     print("语句1")
#     break
#     print("语句2")
# print("语句3")

# 演示break的嵌套应用
# for i in range(1, 6):
#     print("语句1")
#     for j in range(1, 6):
#         print("语句2")
#         break
#         print("语句3")
#     print("语句4")

"""
案例:发工资
"""
# import random
#
# money = 10000
#
# for i in range(1, 21):
#     if money > 0:
#         score = random.randint(1, 10)
#         if score < 5:
#             print(f"员工{i},绩效分{score}分,不发工资,下一位")
#         else:
#             money -= 1000
#             print(f"向员工{i}发放工资1000元,账户余额还剩余{money}元")
#     else:
#         print(f"员工{i}工资发完了,下次再来吧")
#         break

"""
for循环输出99乘法表
"""
# 通过外层循环控制行数
for i in range(1, 10):
    # 通过内层循环中输出每一行的内容
    for j in range(1, i+1):
        print(f"{i}*{j}={i * j} ", end='')
    print("")
