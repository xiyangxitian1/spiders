# -*- conding:utf-8 -*-

# def func_num(num1):
#     result_num = 1
#     i = 1
#     while i <= num1:
#         result_num = result_num * i
#         i += 1
#     print(result_num)
#
# func_num(4)

class digui():
    i = 0

    def func_num(self, num1):
        if num1 == 2:
            return 2
        else:
            return num1 * self.func_num(num1 - 1)


if __name__ == '__main__':
    d = digui()
    result = d.func_num(4)
    print(result)
