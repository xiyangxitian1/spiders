# -*- conding:utf-8 -*-
# 匿名函数

def func_sum(num1, num2):
    return num1 + num2


result = func_sum(1, 2)
print(result)
"""第一种方式（一般不这样用，一艘不接受）"""
func = lambda num1, num2: num1 + num2
result = func(1, 2)
print(result)

# 直接接受返回值
result = (lambda num1, num2: num1 + num2)(1, 2)
print(result)


