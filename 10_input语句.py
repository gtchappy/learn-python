"""
演示Python的input语句
获取键盘的输入信息

1、input()语句的功能是,获取键盘输入的数据
2、可以使用:input(提示信息),用以在使用者输入内容之前显示提示信息
3、要注意无论键盘输入什么类型的数据,获取到的数据永远都是字符串

"""

# print("请输入你的名字")
# name = input()
# print("你的名字是%s" % name)

"""
等同于如下代码
"""

name = input("请告诉我你是谁")
print("你的名字是%s" % name)

"""
输入数字类型
"""

# input语句不论输入什么内容 , 统统都把它当作字符串来判断
num = input("请告诉我你的银行卡密码")
print("你的银行卡密码是%s" % type(num))
# 数据类型转换
num2 = int(num)
print("你的银行卡密码是%s" % type(num2))
