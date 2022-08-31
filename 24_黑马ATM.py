money = 5000000


def query():
    name = str(input("你好,请输入你的姓名"))
    print("-------------查询余额-------------")
    print(f"{name}你好,你的余额剩余:{money}元")


def inquire():
    """
    查询余额函数
    :return: 余额数值
    """
    print(f"当前余额为{money}元")


def deposit():
    """
    存款函数
    :return: 存款后的总额
    """
    global money
    deposit_money = int(input("请输入要存款的数目"))
    money += deposit_money
    print(f"存款成功,当前余额为{money}")


def withdrawal():
    """
    取款函数
    :return:取款后的总额
    """
    global money
    withdrawal_money = int(input("请输入要取款的数目"))
    money -= withdrawal_money
    print(f"取款成功,当前余额为{money}")


def main():
    print("-------------主菜单-------------")
    print("1查询余额")
    print("2存款")
    print("3取款")
    print("4取消")
    return input("请输入你的选择")


query()
while True:
    select = main()
    if select == "1":
        inquire()
    elif select == "2":
        deposit()
    elif select == "3":
        withdrawal()
    elif select == "4":
        exit()
    else:
        print("输入的数据有误")
