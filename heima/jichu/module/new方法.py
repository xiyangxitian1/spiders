class Animal:
    def __init__(self):
        print('animal...')


class Dog(Animal):
    name = '哮天犬'


dog1 = Dog()


# 模拟对象被创建的过程
def Dog_():
    # 1.创建对照，给创建出来的对象在内存空间分配空间
    # 具体分配空间是用内部的C语言实现的
    new_obj = Dog.__new__(Dog)  # new方法是object中的方法，因为它是静态方法，不会自动传递参数
    # 所以要手动传递，传递时，应该传你要创建的类对象的类
    # 等同于下面
    # new_obj = object.__new__(Dog)
    # 2. 对象的初始化，定义属性
    new_obj.__init__()
    # 3.把创建好的对象返回
    return new_obj


dog2 = Dog_()

print(dog1.name)
print(dog2.name)
