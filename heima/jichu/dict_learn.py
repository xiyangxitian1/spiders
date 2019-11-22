# -*- conding:utf-8 -*-
# 字典推导式
# 1~10  "1":1,"2":4
dict1 = {str(i): i ** 2 for i in range(1, 11)}
# print(dict1)

dict2 = {"name": "zhangsan", "age": 12}
dict3 = {dict2[key]: key for key in dict2}
# print(dict3)

"""无序集合推导式"""
list1 = ["beijing", "beihai", "shanghai", "wuhan", "sz", "beijing", "beihai", "heze"]
list2 = [city for city in list1 if city.startswith('b')]
set1 = {city for city in list1 if city.startswith('b')}  # 无序集合推导式 就是把列表推导式的[]换成{}

print(list2)
print(type(list2))
print(set1)
print(type(set1))
