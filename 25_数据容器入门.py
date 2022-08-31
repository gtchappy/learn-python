"""
python 中的数据容器

list(列表)
tuple(元组)
str(字符串)
set(集合)
dict(字典)
"""

"""
列表
注意:列表可以一次存储多个数据,且可以为不同的数据类型,支持嵌套
"""
# 字面量
# [元素1,元素2,元素3,元素4]

# 定义变量
# 变量名称 = [元素1,元素2,元素3,元素4]

# 定义空列表
# 变量名称 = []
# 变量名称 = list()
name_list = ['a', 'b', 'c']
print(name_list)
print(type(name_list))
# 不同类型
my_list = ['a', 666, True]
print(my_list)
print(type(my_list))
# 嵌套列表
my_list = [1, 2, 3], [4, 5, 6]
print(my_list)
print(type(my_list))
