"""
 私有属性和方法
 属性私有化 就是不让此属性在类的外部使用，只能在类的内部使用
 
 在属性名字的前面加上双下划线  就成了私有属性
"""


class Dog:
    def __init__(self):
        self.__age = None

    def eat(self):
        print('吃东西')

    # 定义一对set和get方法  在set方法中对数据进行安全判断，，
    # 后再使用
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            self.__info('age')

    def get_age(self):
        return self.__age

    def __info(self, property_name):
        """
        私有方法也是只能在类的内部使用
        :return:
        """
        print('%s属性赋值不成功' % property_name)


dog1 = Dog()
# dog1.age = -10  # 脏数据 垃圾数据
dog1.set_age(10)
#  不要像下面这样，把公有的属性和私有的属性名字相同
dog1.__age = 12  # 这个是公有的属性__age 和私有的__age是两个不同的属性，只是名字相同

print(dog1.get_age())
print(dog1.__age)
