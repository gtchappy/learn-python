"""
演示文件的写入
"""

# 打开文件，不存在的文件，r，w，a
f = open("C:/Users/gtc/Desktop/lala.txt", "w", encoding="UTF-8")

# write写入
# 内容写入到内存中
# f.write("hello word1!!")

# flush刷新
# 将内存中积攒的内容，写入到硬盘的文件中
# f.flush()

# close将文件关闭
# close方法，内置了flush的功能
# f.close()

# 再次打开文件
f = open("C:/Users/gtc/Desktop/lala.txt", "w", encoding="UTF-8")

# write写入
f.write("我靠")

# close将文件关闭
f.close()
