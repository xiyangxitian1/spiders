class Dog:
    def __init__(self):
        self.name = '狗'


class XTQ(Dog):
    # 如果子类中要定义的新的属性时，需要重写init方法，
    # 重写此方法后，默认父类中的属性不会再继承
    # 如果还想拥有父类中的属性，需要手动调用父类中的init方法

    def __init__(self):
        # super(XTQ, self).__init__()
        super().__init__()
        self.color = 'black'
        # self.name = '哮天犬'  # 这就是修改了


xtq = XTQ()
print(xtq.name)
print(xtq.color)
