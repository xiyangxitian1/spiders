class SweetPotato:
    """
    定义地瓜类
    """

    def __init__(self):
        self.state = '生的'  # 状态
        self.cooked_time = 0  # 烤的时间

    def cook(self, time):
        """
        烤的方法
        :param time: 烤的时间
        :return:
        """
        self.cooked_time += time
        # print('烤地瓜')
        if 3 <= self.cooked_time < 6:
            self.state = '半生不熟'
        elif 6 <= self.cooked_time < 9:
            self.state = '熟了'
        else:
            self.state = '烤糊了'

    def __str__(self):
        return '地瓜当前状态：%s,烤的总时间:%d分钟' % (self.state, self.cooked_time)


digua1 = SweetPotato()
digua1.cook(4)
print(digua1)
digua2 = SweetPotato()
digua2.cook(6)
print(digua2)
digua3 = SweetPotato()
digua3.cook(8)
print(digua3)
digua4 = SweetPotato()
digua4.cook(10)
print(digua4)
