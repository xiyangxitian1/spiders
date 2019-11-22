class Dog:
    def __init__(self):
        self.__type = '狗'  # 私有属性不能被继承
        self.name = '大黄狗'

    def eat(self):
        print('吃饭')

    def __info(self):  # 私有方法不能被继承
        print('小狗')


class XTQ(Dog):

    def see_host(self):
        self.eat()


xiaotq = XTQ()
xiaotq.eat()
print(xiaotq.name)
print(xiaotq.eat())
