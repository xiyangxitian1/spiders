# 定义类
class Dog:

    def eat(self):
        print(self)
        print('%s在吃东西' % self.name)


dog1 = Dog()  # 创建对象
dog1.name = '旺财'  # 第一次给对象的属性赋值就是定义一个属性
print(dog1.name)
dog1.name = '来福'  # 第二次给对象的赋值是修改属性的值
print(dog1.name)

dog1.age = 2  # 一个对象可以有多个属性
dog1.age = 3
print(dog1)
dog1.eat()

dog2 = Dog()
dog2.name = '旺财'
dog2.age = 4
print(dog2)
dog2.eat()

print("{1}真的{0}牛{2}".format('a', 'b', 'c'))
