class Dog:
    def eat(self):
        print('吃东西')


class God:
    def fly(self):
        print('会飞')

    def eat(self):
        print('吃蟠桃')


class XTQ(God, Dog):

    def eat(self):
        # Dog.eat(self)
        # super().eat()
        # super(Dog, self).eat()
        #  继承关系复杂时，想要调用指定父类的方法，直接用指定的父类名.方法名
        Dog.eat(self)


# 尽量不用多继承，会乱，不过有这种需求也可以使用
xtq = XTQ()
# xtq.fly()
xtq.eat()
print(XTQ.__mro__)  # 查看继承链
