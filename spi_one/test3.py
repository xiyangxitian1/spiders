# -*- conding:utf-8 -*-

# 1,1,2,3,5,8,13....

n = 10
i = 0
while True:
    if i == 0 or i == 1:
        a = b = 1
        print(a, end=' ')
    elif i < n:
        a, b = b, a + b
        print(b, end=' ')
    else:
        break
    i += 1

