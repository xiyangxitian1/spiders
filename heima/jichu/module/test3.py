class Animal:
    def __init__(self):
        print('animal')

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        print('dog')

Dog()