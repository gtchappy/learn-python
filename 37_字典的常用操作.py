"""
演示字典的常用操作

    # 字典有如下特点
    1.可以容纳多个数据
    2.可以容纳不同类型的数据
    3.每一份数据是KeyValue键值对
    4.可以通过Key获取到Value，Key不可重复(重复会覆盖)
    5.不支持下标索引
    6.可以修改(增加或删除更新元素等)
    7.支持for循环，不支持while循环
"""
my_dict = {"王力宏": 99, "周杰伦": 97, "林俊杰": 93 }

# 新增元素
my_dict["张兴哲"] = 77
print(f"字典经过新增元素后，结果：{my_dict}")

# 更新元素
my_dict["周杰伦"] = 33
print(f"字典经过更新后，结果：{my_dict}")

# 删除元素
score = my_dict.pop("周杰伦")
print(f"字典中被移除了一个元素，结果：{my_dict}，周杰伦的考试分数是：{score}")

# 清空元素
my_dict.clear()
print(f"字典被清空了，内容是：{my_dict}")

# 获取全部key
my_dict = {"王力宏": 99, "周杰伦": 97, "林俊杰": 93, }
keys = my_dict.keys()
print(f"字典的全部keys是：{keys}")

# 遍历字典
# 方式1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

# 方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"2字典的key是：{key}")
    print(f"2字典的value是：{my_dict[key]}")

# while循环不能用，因为字典不支持下标序列

# 统计字典内的元素数量，len()
num = len(my_dict)
print(f"字典中的元素数量有：{num}个")
