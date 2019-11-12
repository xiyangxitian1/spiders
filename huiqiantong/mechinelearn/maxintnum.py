import sys
import math

max = sys.maxsize
print(max)

flag = False
for i in range(1 - max, max):
    for j in range(1 - max, max):
        for k in range(1 - max, max):
            if math.pow(i, 3) + math.pow(j, 3) + math.pow(k, 3) == 114:
                print(i, j, k)
                flg = True
                break
        if flag:
            break
    if flag:
        break

print('执行完毕')
