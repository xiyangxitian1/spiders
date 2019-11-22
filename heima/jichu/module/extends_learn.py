class Dog(object):  # 新式类写法  所有的类最终都会继承到object
    def eat(self):
        print(self)
        print('吃东西')


# 继承：想要拥有某个类的方法或属性时  子类继承了父类之后，
# 就可以拥有父类中的所有的方法和属性
# 语法格式 类名（写上要继承的类/父类)
class XTQ(Dog):
    """啸天犬 """
    # def eat(self):
    #     print('吃东西')


xiaotq = XTQ()
print(xiaotq)
xiaotq.eat()
