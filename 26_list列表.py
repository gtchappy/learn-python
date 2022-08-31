"""
演示数据容器之:list列表
语法:[元素,元素,...]
"""
# 定义一个列表
name_list = ['a', 'b', 'c']
print(name_list)
print(type(name_list))

my_list = ['a', 666, True]
print(my_list)
print(type(my_list))

# 定义一个嵌套的列表
my_list = [1, 2, 3], [4, 5, 6]
print(my_list)
print(type(my_list))

# 通过下标索引取出对应位置的数据

"""
1. 列表的定义语法
[元素1,元素2,元素3...]
2. 什么是元素
数据容器内的每一份数据,都称之为元素
3. 元素的类型有限制吗
元素的数据类型没有任何限制,甚至元素也可以是列表,这样就定义了嵌套列表
"""

# 通过下标索引取出对应位置的数据
my_list = ["Tom", "Lily", "Rose"]
# 列表[下标索引],从前向后从0开始,每次+1,从后向前-1开始,每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])
# 错误示范,通过下标索引取数据,一定不要超出范围
# print(my_list[3])

# 通过下标索引取出数据(倒序取出，从-1开始)
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# 取出嵌套列表的元素
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[1][1])
