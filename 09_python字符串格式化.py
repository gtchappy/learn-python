num = 11
num2 = 11.345
print("数字11宽度限制5,结果是:%5d" % num)
print("数字11宽度限制1,结果是:%1d" % num)
print("数字11宽度限制7,小数精度2:结果是:%7.2f" % num2)
print("数字11宽度限制7,小数精度2:结果是:%.2f" % num2)
"""
字符串格式化的方式:f"{占位}"
"""

name = "传智播客"
set_up_year = 2006
stock_price = 19.99

# f:format
print(f"我是{name},我成立于:{set_up_year}年,我今天的股价是:{stock_price}")
print("我是", name, "我成立于", set_up_year, "年,我今天的股价是:", stock_price)
