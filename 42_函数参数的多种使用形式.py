def user_info(name, age, gender):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")


# 位置参数 - 默认使用形式
user_info("小明", 20, "男")

# 关键字参数
user_info(name='小王', age=11, gender='女')
user_info(age=21, name='小力', gender='男')
user_info('甜甜', gender='女', age=9)


# 缺省参数
# 缺省参数一定要写在最后面
def user_info(name, age, gender='男'):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")


user_info('小明', 11)
user_info('小天', 22, "女")


# 不定长 - 位置不定长，*号
# 不定长定义的形式参数会作为（元组）存在，接收不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)},内容是：{args}")


user_info(1, 2, 3, '小明', '男孩')


# 不定长 - 关键字不定长，**号
def user_info(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)},内容是：{kwargs}")


user_info(name='小王', age=11, 性别='男孩')
