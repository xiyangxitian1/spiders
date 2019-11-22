# 当try里面的代码出现异常后，它会自动创建一个指定类型的异常对象
# except中 as后面的变量将来就会接收到异常对象
# 我们print error就是在输出异常对象，它内部帮我们实现str方法
# 所以输出对象时 有相应的内容
try:
    raise NameError('异常信息')  # 手动创建异常对象并抛出
# error = NameError('异常信息')
# 抛出异常后会自动把异常对象赋值给 as 后面的变量
except NameError as error:
    print('提示： %s' % error)


# 自定义异常类  自定义异常类，必须继承Exception
class CustomException(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'CustomException:%s' % self.name


try:
    phone_num1 = input('请输入电话号码：')
    if len(phone_num1) != 11:
        # print('手机号码不对')
        raise CustomException('手机号码不对')
    phone_num2 = input('请输入电话号码：')
    if phone_num2.isdecimal() is False:
        raise CustomException('手机号码不合法')
        # print('手机号码不合法')
except CustomException as error:
    print(error)
