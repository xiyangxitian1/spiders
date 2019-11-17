import matplotlib.pyplot as plt
import numpy as np

# 散点图
x = [1, 2, 3, 4, 5, 6]
y = [i * 4 for i in x]

x = np.random.normal(0, 1, 64)
y = np.random.normal(0, 1, 64)
S = np.random.rand(64) * 500  # 大小
C = np.random.rand(64)  # 颜色  要结合cmpa(colormap)来使用
# alpha 透明度
plt.scatter(x, y, marker='*', s=S, c=C, cmap='plasma', alpha=0.6)

plt.show()
