class Dog:
    type = '狗1'
    __type__ = '狗'  # 类属性也可以私有化，只能在类中访问

    def __init__(self):
        self.name = '小花'
        # self.type = '狗'
        self.__type__ = '小狗'


dog1 = Dog()
dog1.name = '旺财'
print(dog1.name)

dog2 = Dog()
dog2.name = '来福'

# 设置类属性的值
Dog.type = '狗class'  # 类对象只能用类对象去修改它的值

print(Dog.type)  # 类对象和实例对象都能访问类属性
print(dog2.type)
