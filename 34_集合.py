"""
# set 代表集合
首先，因为集合是无序的，所以集合不支持:下标索引访问
集合不支持下标索引！！！！！！


# 集合有如下特点
    1.可以容纳多个数据
    2.可以容纳不同类型的数据(混装)
    3.数据是无序存储的(不支持下标索引)！！！！！！
    4.不允许重复数据存在！！！！！！！！！！！！！
    5.可以修改(增加或删除元素等)
    6.支持for循环
"""
# 定义集合

my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima"}
my_set_empty = set()  # 定义空集合
print(f"my_set的内容是：{my_set},类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty},类型是：{type(my_set_empty)}")

# 添加新元素
my_set.add("python")
my_set.add("传智教育")  # 因为已经有"传智教育"了，所以不能再添加
print(f"my_set添加元素后结果是：{my_set}")

# 移除元素
my_set.remove("黑马程序员")
print(f"my_set移除黑马程序员后，结果是：{my_set}")

# 随机取出元素
my_set = {"传智教育", "黑马程序员", "itheima"}
element = my_set.pop()  # 因为集合没有下标所以是随机取出一个元素
print(f"集合被取出元素是：{element}")

# 清空集合
my_set.clear()
print(f"集合被清空啦，结果是：{my_set}")

# 取出2个集合的差集
# 语法：集合1.different(集合2),功能:取出集合1和集合2的差集(集合1有而集合2没有的)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"取出差集后的结果是：{set3}")
print(f"取差集后，原有set1的内容：{set1}")
print(f"取差集后，原有set2的内容：{set2}")

# 消除2个集合的差集(消除两个集合里面相同的)
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"消除差集后，集合1结果：{set1}")
print(f"消除差集后，集合2结果：{set2}")

# 2个集合合并为1个
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"2集合合并结果：{set3}")
print(f"合并后集合1：{set1}")
print(f"合并后集合2：{set2}")

# 统计集合元素数量len()
set1 = {1, 2, 3, 4, 5, 5, 5, 5, 5}
num = len(set1)
print(f"集合内的元素数量有：{num}个")  # 何并去重再算的

# 集合的遍历
# 集合不支持下标索引，不能用while循环
# 可以用for循环
set1 = {1, 2, 3, 4, 5, 6}
for element in set1:
    print(f"集合的元素有：{element}")
