import matplotlib.pyplot as plt

# 线性图

x = [1, 2, 3, 4, 5, 6]
y = [i * 3 for i in x]  # 列表推导式
y2 = [i + 4 for i in x]
# y = [2, 5, 8, 9, 11, 30]
plt.plot(x, y, marker='v', color='red', linewidth=6, linestyle=':', label='y=3x')  # lineWidth 线条的粗细
plt.plot(x, y2, color='green', label='y=x+4')
plt.xlabel('Price')  # x坐标轴的名
plt.ylabel('Sales')  # y坐标轴的名
plt.legend(loc='lower right')  # 显示设置的label  显示线的名

plt.xlim(0, 10)  # 设置x轴的取值范围
# plt.xticks()  # 显示x的刻度
plt.yticks([0, 5, 10, 15], ['0', '5', '10', '15'])
plt.show()
