# 让对象只分配一次内存，只让它执行一次new方法就可以


class ShoppingCart:
    """购物车类"""

    __single_instance = None  # 记录创建出来的对象
    __has_init = False  # 记录对象是否初始化过了，默认没有初始化

    def __new__(cls, *args, **kwargs):
        """重写创建对象的方法"""
        if cls.__single_instance is None:
            cls.__single_instance = object.__new__(cls)
        # 如果已经创建过了对象直接返回创建的对象
        return cls.__single_instance

    def __init__(self):
        if not ShoppingCart.__has_init:  # if ShoppingCart.__has_init is False
            self.total_price = 0
            ShoppingCart.__has_init = True


cart1 = ShoppingCart()
cart1.total_price = 200
print(cart1.total_price)

cart2 = ShoppingCart()
print(cart2.total_price)
