n = 10
list = []
for i in range(n):
    if i == 0 or i == 1:  # 前2项为1
        list.append(1)
    else:
        list.append(list[i - 2] + list[i - 1])  # 为前两项值之和
print(list)
