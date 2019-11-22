class Dog:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        """
        当对象要从内存空间中回收时，从内存中删除时就会自动调用此方法
        此方法调用说明对象即将销毁，可以在此方法做"临终遗言"  判断此对象是否被销毁
        :return:
        """
        print('%s 要被删除了，销毁了' % self.name)
        print(self.name)


dog1 = Dog('旺财')
a = dog1
del dog1  # 删除对象时会立即执行 __del__   ，不删除时会等程序全部执行完成时销毁
print('**')

def main():
    dog1 = Dog('xx')

main()

print('_____________________')