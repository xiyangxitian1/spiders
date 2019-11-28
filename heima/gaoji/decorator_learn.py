class Logging(object):
    def __init__(self, func):
        print('init1...')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('call...')
        return self.func(*args, **kwargs)


class Logging2(object):
    def __init__(self, level='INFO'):
        print('init2...')
        self.level = level

    def __call__(self, func):  # 接受函数
        def wrapper(*args, **kwargs):
            if self.level == 'a':
                print('a')
            else:
                print('b')
            func(*args, **kwargs)

        return wrapper  # 返回函数


@Logging
def say(something):
    print('say {}'.format(something))


@Logging2(level='a')
def say2(something):
    print('say2 {}'.format(something))


say2('hello')
# say2('hello world')
