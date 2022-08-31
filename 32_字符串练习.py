my_str = "itheima itcast boxuegu"
new_str = my_str.replace(" ", "|")
print(f"{my_str}替换后的字符串为{new_str}")

new_str2 = new_str.split("|")
print(f"{new_str}按照|分割后得到的列表是{new_str2}")
''