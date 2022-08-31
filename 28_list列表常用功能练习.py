my_list = [21, 25, 21, 23, 22, 20]
# 在列表尾部追加一个数字31
my_list.append(31)
# my_list.insert(6, 31)

# 追加一个新列表[29,33,30]
my_list2 = [29, 33, 30]
my_list.extend(my_list2)
# 取出第一个元素
print(my_list[0])
# 取出最后一个元素
print(my_list[6])
# 查找元素31，在列表中的下标位置
# print(my_list)
my_index = my_list.index(31)
print(my_index)
