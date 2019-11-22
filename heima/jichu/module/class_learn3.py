class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 2

    def eat(self):
        print('%s吃东西' % self.name)

    # 此方法是用print输出对象时自动调用，它会把此方法返回出来的字符串输出
    def __str__(self):  #
        return '我是%s,今年%d岁了' % (self.name, self.age)


dog1 = Dog('旺财')
dog1.eat()

dog2 = Dog('来福')
dog2.eat()

print(dog1)  # 调用了__str__
