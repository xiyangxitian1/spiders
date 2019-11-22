"""
你好，以下是3道测试题，请直接在网页答题，限时30分钟。完成后通知HR
~
注意：不要借助第三方工具，如编辑器；也不要复制粘贴。否则视为无效答题！
综上，请直接手写代码

1.
给定长度n，返回长度为n的斐波那契数列
"""

n = 10
list = []
for i in range(n):
    if i == 0 or i == 1:
        list.append(1)
    else:
        list.append(list[i - 1] + list[i - 2])
print(list)


# 2.
# 输入m, n(1 < m < n < 1000000)，返回区间[m, n]
# 内的所有素数的个数


def test2(m, n):
    list = []
    for i in range(m, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list.append(i)
    return len(list)


# 3.
# n个人排成一列，每人手里面有0
# ~n - 1
# 个球，如果有两人手中拥有同样数量的球，返回球的数量（如果有多组只需返回任意一组即可），否则返回 - 1
# 例如：给定lst = [2, 4, 1, 0, 5, 3, 2, 3]
# 表示8人手中拥有的球的数量，返回值输出2或者3都是可行的
# 注：空间复杂度 <= O(n), 时间复杂度 <= O(n), 不能借助set, dict数据结构


def getNum(lst):
    list = []
    count = 0
    for i in range(len(lst)):
        if i != lst.index(lst[i]):
            if lst[i] not in list:
                list.append(lst[i])
    else:
        return list
