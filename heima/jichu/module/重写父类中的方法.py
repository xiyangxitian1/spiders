class Dog(object):  # 新式类写法  所有的类最终都会继承到object
    def eat(self):
        print(self)
        print('吃东西')


# 继承：想要拥有某个类的方法或属性时  子类继承了父类之后，
# 就可以拥有父类中的所有的方法和属性
# 语法格式 类名（写上要继承的类/父类)
class XTQ(Dog):
    """啸天犬 """

    # 如果子类有和父类同名的方法  执行时，优先调用自己里面的方法
    def eat(self):
        """
        在子类中定义了一个和父类同名的方法，就叫重写父类方法
        继承链  当前类->直接父类 --> ... --> object所有类的方法
        """

        print('吃仙桃')


xiaotq = XTQ()
# print(xiaotq)
xiaotq.eat()
