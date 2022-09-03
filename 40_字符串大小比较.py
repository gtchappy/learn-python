"""
演示字符串大小比较
    #字符串如何比较
    从头到尾，一位位进行比较，其中一位大，后面就无需比较了
    #单个字符之间如何确定大小
    通过ASCII码，确定字符对应的码值数字来确定大小
"""

# abc 比较 abd
print(f"abc大于abd，结果：{'abd' > 'abc'}")

# a比较ab
print(f"abd大于abc，结果：{'abd' > 'abc'}")

# a比较A
print(f"a大于A，结果：{'a'>'A'}")

# key1比较key2
print(f"key2>key1，结果：{'key2'>'key1'}")
