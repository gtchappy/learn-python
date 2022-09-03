"""
统计文件中有几个'itheima'
"""
# 方法一：运用read()和count()
# with open("C:/Users/gtc/Desktop/test.txt", "r", encoding="UTF-8") as f:
#     lines = f.read()
#     print(f"文件的内容是：{lines}")
#     num = lines.count('itheima')
#     print(f"itheima 有{num}个")

# 方法二：读取内容，一行一行读取
with open("C:/Users/gtc/Desktop/test.txt", "r", encoding="UTF-8") as f:
    count = 0
    for line in f:
        line = line.strip()  # 去除开头和结尾的空格以及换行符
        words = line.split(" ")
        print(line)
        for word in words:
            if word == 'itheima':
                count += 1
    print(f"itheima出现了{count}次")
