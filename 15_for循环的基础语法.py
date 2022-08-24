"""
演示for循环的基础语法
for循环也成为遍历循环
"""

"""
 name = "ithema"

 for x in name:
     将name的内容,挨个取出赋予x临时变量
     就可以在循环体内对x进行处理
     print(x)
"""


"""
数一数有几个'a'
"""

# 统计如下字符中,有多少个字母a
name = "itheima is a brand of itcast"
# 定义一个变量,用来统计有多少个a
count = 0
# for 循环统计
# for 临时变量 in 被统计的数据:
for x in name:
    if x == "a":
        count += 1
print(f"被统计的字符串中有{count}个a")
