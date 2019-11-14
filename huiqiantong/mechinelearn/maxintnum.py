import sys
import math

# max = sys.maxsize
max = 1000
print(max)
print(-max)

flag = False
for i in range(-max, max):
    if i % 10 == 0:
        print("i=", i)
    for j in range(-max, max):
        for k in range(-max, max):
            if math.pow(i, 3) + math.pow(j, 3) + math.pow(k, 3) == 114:
                print(i, j, k)
                flag = True
                break
        if flag:
            break
    if flag:
        break

print('执行完毕')
