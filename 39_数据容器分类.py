# 数据容器可以从以下视角进行简单的分类：
"""
    #是否支持下标索引：
        #支持：列表、元组、字符串   -序列类型
        #不支持：集合、字典   -非序列类型
    #是否支持重复元素：
        #支持：列表、元组、字符串   -序列类型
        #不支持：集合、字典  -非序列类型
    #是否可以修改
        #支持：列表、集合、字典
        #不支持：元组、字符串
"""

# 基于各类数据容器的特点，它们的应用场景如下：
"""
    #列表：一批数据，可修改、可重复的存储场景
    #元组：一批数据，不可修改、可重复的存储场景
    #字符串：一串字符串的存储场景
    #集合：一批数据，去重存储场景
    #字典：一批数据，可用Key检索Value的存储场景
"""

# 数据容器的通用操作
"""
    -遍历
        5类容器都支持for循环遍历
        列表、元组、字符串支持while循环，集合、字典不支持(无法下标索引)
        
        尽管遍历的形式各有不同，但是，它们都支持遍历操作
"""
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# len元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串 元素个数有：{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有：{len(my_dict)}")

# max最大元素
print(f"列表 最大的元素是：{max(my_list)}")
print(f"元组 最大的元素是：{max(my_tuple)}")
print(f"字符串 最大的元素是：{max(my_str)}")
print(f"集合 最大的元素是：{max(my_set)}")
print(f"字典 最大的元素是：{max(my_dict)}")

# min最小元素
print(f"列表 最小的元素是：{min(my_list)}")
print(f"元组 最小的元素是：{min(my_tuple)}")
print(f"字符串 最小的元素是：{min(my_str)}")
print(f"集合 最小的元素是：{min(my_set)}")
print(f"字典 最小的元素是：{min(my_dict)}")

# 类型转换：容器转列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")

# 类型转换：容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"元组转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组的结果是：{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是：{tuple(my_dict)}")

# 类型转换：容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")
print(f"元组转字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串的结果是：{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}")

# 类型转换：容器转集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合的结果是：{set(my_str)}")
print(f"集合转集合的结果是：{set(my_set)}")
print(f"字典转集合的结果是：{set(my_dict)}")

# dict(my_list)
# 会报错，因为不是键值对

"""
通用排序功能：
sorted(容器,[reverse=True]
"""
# 进行容器的排序
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "abcdefg"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

print(f"列表对象的排序结果是：{set(my_list)}")
print(f"元组对象的排序结果是：{set(my_tuple)}")
print(f"字符串对象的排序结果是：{set(my_str)}")
print(f"集合对象的排序结果是：{set(my_set)}")
print(f"字典对象的排序结果是：{set(my_dict)}")
