# 单例模式 (自己凭经验写的)
class Dog:
    __obj = None

    @staticmethod
    def get_single_dog():
        if Dog.__obj is None:
            __obj = Dog.__new__(Dog)  # __new__方法是静态的所以要，手动传递参数
            __obj.__init__()
            Dog.__obj = __obj

        return Dog.__obj


dog1 = Dog.get_single_dog()
dog2 = Dog.get_single_dog()
print(dog1)
print(dog2)
