# 带参数的类装饰器
class Logging(object):
    def __init__(self, level='log'):
        print(level)
        self.level = level

    def __call__(self, fun):
        def wrapper(*args, **kwargs):
            if self.level == 'a':
                print('call..')
            else:
                print('call..other...')
            fun(*args, **kwargs)

        return wrapper


class Logging1(object):
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        self.__fn(*args, **kwargs)


#  带参数的类装饰器要必须要加参数，否则运行结果是不对的。会把函数当作参数。
@Logging(level='b')
def say(something):
    print(something)

# say('hello world')
