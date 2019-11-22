list1 = [1, 2]

list2 = [1, 2]
# list2 = list1
print(id(list1))
print(id(list2))

# ==是判断两侧的数据值是否相等
if list1 == list2:
    print("==成立")
# is判断的是两侧变量引用的内存地址是否相同
if list2 is list1:
    print('成立')
else:
    print('不成立')

# None True False 这种情况尽量用is   其实情况一般都是用==
# is性能会比==高  因为只读内存地址  而==要到内存地址的值

