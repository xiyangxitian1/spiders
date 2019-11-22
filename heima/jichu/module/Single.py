class Dog:
    __instance = None
    __has_init = False

    def __new__(cls, *args, **kwargs):
        if Dog.__instance is None:
            Dog.__instance = object.__new__(cls)
        return Dog.__instance

    def __init__(self, name):
        # self.name = name  # 不能这样写 因为只有一个对象，所以name是最后创建的一个对象的值
        # 所以也不需要传参数，没什么意义
        if not Dog.__has_init:
            self.type = '狗'


dog1 = Dog('小狗')

print(dog1)
print(dog1.name)
dog2 = Dog('大黄狗')
print(dog2)
print(dog2.name)
