"""
面向对象语言三大特性
1.封装：把数据和操作都变成属性 方法 封装在类的内部
2.继承 想要有某个类的属性和方法时
3.多态： 在使用父类对象的时候，也可以使用子类的对象
鸭子类型:不强求数据的真实类型，只要可以完成相应的操作，不报错就行，动态语言独有的特性
"""


class Meat:
    def __init__(self):
        self.name = '肉'


class Ham(Meat):
    pass
# def __init__(self):
#     super(Ham, self).__init__()
#     self.name = '火腿'


class Ji:
    def __init__(self):
        self.name = '鸡肉'


class Person:
    # 这是动态语言独有的特性 ： 鸭子类型
    def eat(self, xxx):  # 这个meat不管是什么类型  只要有name属性就行
        print('吃：%s' % xxx.name)


m1 = Meat()
h1 = Ham()
ji = Ji()

p = Person()
p.eat(m1)
p.eat(h1)
p.eat(ji)
