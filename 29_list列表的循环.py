"""
演示对list列表的循环，使用while和for循环2种方式

while循环和for循环，都是循环语句，但细节不同
在循环控制上：
    while循环可以自定循环条件，并自行控制
    for循环不可以自定循环条件，只可以一个个从容器内取出数据
在无限循环上：
    while循环可以通过条件控制做到无限循环
    for循环理论上不可以，因为被遍历的容器容量不是无限的
在使用场景上：
    while循环适用于任何想要循环的场景
    for循环适用于，遍历数据容器的场景或简单的固定次数循环场景
"""


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    my_list = ["传智教育", "黑马程序员", "Python"]
    # 循环控制变量通过下标索引来控制，默认0
    # 每一次循环将下标索引变量+1
    # 循环条件：下标索引变量 < 列表的元素数量

    # 定义一个变量用来标记列表的下标
    #  初始值为0
    index = 0
    while index < len(my_list):
        # 通过index变量取出对应下标的元素
        element = my_list[index]
        print(f"列表的元素：{element}")

        # 至关重要 将循环变量(index)每一次循环都+1
        index += 1


list_while_func()


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:None
    """
    my_list = [1, 2, 3, 4, 5]
    # for  临时变量  in 数据容器
    for element in my_list:
        print(f"列表的元素有：{element}")


list_for_func()
