"""
演示数据容器字典的定义
"""

# 定义字典
my_dict = {"王力宏": 99, "周杰伦": 97, "林俊杰": 93, }

# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是：{my_dict}，类型：{type(my_dict)}")
print(f"字典2的内容是：{my_dict2}，类型：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3}，类型：{type(my_dict3)}")

# 定义重复key的字典
my_dict1 = {"王力宏": 99, "王力宏": 88, "周杰伦": 97, "林俊杰": 93, }
print(f"重复key字典的内容是：{my_dict1}")

# 从字典中基于key获取value
my_dict4 = {"王力宏": 99, "周杰伦": 97, "林俊杰": 93, }
score = my_dict4["王力宏"]
print(f"王力宏的考试分数是：{score}")

# 定义嵌套字典
stu_score_dict = {
    "王力宏": {
        "语文": 77,
        "英语": 88,
        "数学": 99
    }, "周杰伦": {
        "语文": 73,
        "英语": 82,
        "数学": 91
    }, "林俊杰": {
        "语文": 75,
        "英语": 88,
        "数学": 90
    },
}
print(f"学生的考试信息是：{stu_score_dict}")

# 从嵌套字典中获取数据
# 看一下周杰伦的语文信息
score = stu_score_dict["周杰伦"]["语文"]
print(f"周杰伦的语文分数是：{score}")
score = stu_score_dict["林俊杰"]["英语"]
print(f"林俊杰的语文分数是：{score}")

