# import sys
# print(sys.path)
# 当外面用 from module import * 的方式导入此模块时
# 可以用引变量来控制导入的具体
__all__ = ['func','count']

def func():
    print('func')


count = 10


class Dog:
    pass
