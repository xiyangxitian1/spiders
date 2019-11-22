class Dog:
    __type = '狗'  # 类属性也可以私有化，只能在类中访问

    # 语法糖  只要在方法上加了这个@classmethod 后面的第一个方法，就是类方法
    # 类方法的第一个形参自动变成 类对象，将来调用时，类方法的第一形参自动传递
    # 传递调用此方法的类对象
    @classmethod
    def get_type(cls):
        return cls.__type

    # 类方法一般是结合类属性使用
    @classmethod
    def set_type(cls, type):
        cls.__type = type


# cls == Dog  # cls等同于Dog
# 类方法一般用类对象去调用，但它也可以实例对象调用
print(Dog.get_type())
dog1 = Dog()
print(dog1.get_type())
