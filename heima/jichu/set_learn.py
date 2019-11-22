# -*- conding:utf-8 -*-
"""
set不会有重复的数据
作用：可以把列表或元组中的数据去重
"""
# set1 = {1, 2, 3, 4, 2, 3, 5}
# print(set1)
# print(type(set1))

list1 = [1, 2, 3, 2, 3]
i = 0
result = []
while i < len(list1):
    element = list1[i]
    index = list1.index(element)  # 获取当前元素在列表中第一次出现的索引
    if index == i:  # 此元素第一次出现
        result.append(element)
    i += 1

print(result)

result2 = list(set(list1))  # 用set来去重
print(result2)

tuple1 = (1, 2, 1,)
tuple2 = tuple(set(tuple1)) # 用set去重tuple
print(tuple2)


