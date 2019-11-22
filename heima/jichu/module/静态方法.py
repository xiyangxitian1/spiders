class Dog:

    @staticmethod
    def fly():
        print('飞一会~')

    @staticmethod
    def eat():
        print('吃东西')


dog1 = Dog()
dog1.eat()
Dog.eat()
Dog().eat()


