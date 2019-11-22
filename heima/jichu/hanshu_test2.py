# -*- conding:utf-8 -*-

def test1(*a, **b):
    print(a)
    print(b)
    print('*' * 58)
    #  手动解包 (a,b)-> a,b  **b -> d=4
    # 这种用法只能在实参的时候使用
    test2(*a, **b)


def test2(*a, **b):
    print(a)
    print(b)
    print('test2:', a, b)


a, b, c = 1, 2, 3
# 函数会自动的组包 把a与b当成是第一个参数(a,b)  第二个参数为{'d':4}
test1(a, b, d=4)
