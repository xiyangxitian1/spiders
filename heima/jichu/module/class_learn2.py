class Dog:
    # 给init方法添加相应的形参，叫自定义初始化方法，（自定义构造方法）
    # 创建对象时，就会自动调用init 初始化方法
    def __init__(self, name='旺财'):  # __xx__魔法方法（官方解释叫：运算符重载方法）  它会在特殊情况下自动调用
        # 初始化方法，此方法中定义对象公共属性
        self.type = '狗'
        self.name = name
        print(self.__class__)
        print(self.__dict__)  # 这个对象的所有属性

    def eat(self):
        print('吃东西')


dog1 = Dog('小小')
print(dog1.type)
print('----------')
Dog.__init__(dog1)



