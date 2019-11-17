import matplotlib.pyplot as plt
import numpy as np

# 柱状图
x = np.arange(1, 13)
print(x)
y = np.random.uniform(0.5, 1.0, 12) * (1 - x / float(13))
# y = np.random.uniform(0.1, 1.0, 12)
plt.bar(x, y, facecolor='green', edgecolor='black')
plt.ylim(0, 1)  # y的取值范围
for x, y in zip(x, y):
    # 柱子上的值显示2位小数，位置居中
    plt.text(x + 0.05, y + 0.02, '%.2f' % y, ha='center', va='center')  # 要写的字的位置  x,y是坐标的位置

# 显示图形
plt.show()



