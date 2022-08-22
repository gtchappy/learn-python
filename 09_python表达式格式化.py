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
"""
对表达式进行字符串格式化
f"{表达式}"
"%s\%d\%f" % (表达式、表达式、表达式)
"""
print("表达式格式化")
print("1*1的结果是:%d" % (1 * 1))
print(f"1*2的结果是:{1 * 2}")
print("字符串在python中的类型名是:%s" % type("字符串"))

name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
final_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print(
    f"公司:{name},股票代码:{stock_code},"
    f"当前股价:{stock_price},"
    f"每日增长系数是:{stock_price_daily_growth_factor}"
)
print(
    "经过%d天的增长后," % growth_days,
    "股价达到了:%.2f" % final_stock_price
)
