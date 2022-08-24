# 定义函数进行文档说明
def add(x, y):
    """
    add函数可以接受2个参数,进行2数相加的功能
    :param x:表示相加的1个数字
    :param y:表示相加的另1个数字
    :return:两数相加结果
    """
    result = x + y
    print(f"2数相加的结果是:{result}")
    return result


add(5, 6)


