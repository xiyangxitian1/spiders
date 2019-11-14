import numpy as np
import matplotlib.pyplot as plt
import scipy.misc

# 创建数组
# arr1 = np.array([1, 2, 3])
# print(arr1)
# arr2 = np.array([arr1, [4, 5, 6]])
# print(arr2)

# 创建等差数组
# arr3 = np.arange(10)
# print(arr3)
# arr4 = np.arange(0, 101, 5)
# print(arr4)

# arr5 = np.linspace(0, 10, 6)
# print(arr5)

# 生成数组有默认值
# ones = np.ones((3, 4), dtype='int')
# print(ones)
# # 广播机制  扩展维度
# ones = ones * 8
# print(ones)

# eye = np.eye(6, k=1, dtype='int')
# print(eye)

# zeros = np.zeros((4, 6), dtype='int')
# print(zeros)

# 随机取值
# arr6 = np.random.randint(1, 10, (3, 4))
# print(arr6)

# 索引，切片
# 变量名[index]
# 变量名[start:end]
# arr6[0]
# print(arr6[0])
# print(arr6[-1][2])
# print(arr6[1:2])
# print(arr6[1:2, 1:3])  # 访问某几行的某几列，逗号前面表示行的切片或索引，逗号后面表示列的切片或索引

# shpe形状

# print(arr6)
# print(arr6.reshape(2, 6))
# print(arr6.reshape(4, 3))
# print("***************")
# # 不确定维度的时候可以用-1
# print(arr6.reshape(-1, 3))  # 只知道总数可以被3整除，不知道是多少行，就可写为-1

# 矩阵的转置
# arr8 = arr6.transpose()
# print(arr8)

pic = scipy.misc.ascent()  # pic是一个矩阵
xmax = pic.shape[0]
ymx = pic.shape[1]
pic[range(xmax), range(ymx)] = 0  # 设置对角线
plt.imshow(pic)
plt.show()
# print(pic)
