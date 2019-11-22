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
    # Parameter 参数  形参
    # arguments 参数 实参
    # self表示的是对象
    def eat(self):
        # 方式一
        # 1 Dog.eat(self)  # 用调用方法时，需要手动传self 其它情况不要传

        # 方式二
        # 2 super(指定类,对象).方法
        # 2 super(XTQ, self).eat()  # 继承链 查找指定类在继承类中的下一个父类
        # 方式二的简写
        super().eat()  # 2 上面的方式的简写 一般都是用这种方式
        # super(XTQ, self).eat() # pycharm会自动生成这个形式
        """
        在子类中定义了一个和父类同名的方法，就叫重写父类方法
        继承链  当前类->直接父类 --> ... --> object所有类的方法
        """

        print('吃仙桃')

# xiaotq = XTQ()
# XTQ.eat(xiaotq)
# xiaotq.eat()
# XTQ.eat(XTQ())  这种写法也是可以的，但是不通用
# 类是类对象 所以可以XTQ.eat()
