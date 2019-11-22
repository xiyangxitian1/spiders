# -*- conding:utf-8 -*-
# 查看使用帮助
# help(range)

# range 官方解释：整数序列
# 结合for循环计数实现

# result = range(5)
# class range(object):
# print(type(result))  # <class 'range'>  说明是一个range对象

# print(list(range(1, 3, 5))) 1
list1 = [i for i in range(1, 101)]
# print(list1)
list1 = [i + 1 for i in range(100)]
# 生成一个1~10之间的偶数列表
# list2 = [i for i in range(2, 10, 2)]
# print(list2)
list2 = [i for i in range(1, 11) if i % 2 == 0]
# print(list2)
# list3 = [i for i in range]
# 生成一个列表，中的10个元素都是666
list4 = [666 for _ in range(10)]  # 使用这个值，就使用 _  这个是约定俗成的
# print(list4)
# 取出名字长度大于等于5的
list5 = ['zhangsan', 'lisi', 'wangwu']
list6 = [name for name in list5 if len(name) >= 5]
print(list6)