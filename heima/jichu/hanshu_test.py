# -*- conding:utf-8 -*-

a = 1


def update_a(b):
    global a
    a = b


print(a)
update_a(3)
print(a)
