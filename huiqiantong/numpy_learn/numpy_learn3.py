import numpy as np
import matplotlib.pyplot as plt
import scipy.misc

# 这些np和plt已经是约定俗成的使用简写

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr1)
# print(arr2)
# arr3 = np.arange(start=0, stop=10, step=1)
# print(arr3)
# arr4 = np.linspace(0, 10, 20)  # 生成20个数据，包括10，和arange有区别的  等差数列
# print(arr4)
# 3个特殊的矩阵 zeros ones eye
# zero = np.zeros((3, 5),dtype='int32')   #  生成全部为0的矩阵
# print(zero)
# one = np.ones((3, 4))
# print(one)
# eye = np.eye(6)
# print(eye)

arr5 = np.random.randint(1, 5, (2, 3))  # 从【1，5）取(2,3)矩阵
# print(arr5)
#
# print(arr5.ndim)  # 查看维度信息  2维的
# print(arr5.dtype)  # 查看数据类型  拿到数据的时候先查看数据类型
# print(arr5.shape)  # 形状信息(2,3) 这个是很重要的 机器学习中会用到  有时还要做形状变换
# arr6 = arr5.reshape(3, 2)  # 这个reshape要确定能变成相应的形状
# arr6 = arr5.reshape(3, -1)
# print(arr6)
arr7 = np.array([1, 2, 3, 4, 5])
arr8 = np.array([6, 7, 8, 9, 10])
arr78 = arr7 + arr8  # 这个是很高的，比python的for循环要高很多  原理是什么再说
# print(arr78)
# print(np.sin(arr7))  # 正弦函数

# 矩阵的转置  (行变成了列，列变成了行)
arr9 = [arr5.transpose()]
# print(arr5)
# print("*" * 80)
# print(arr9)

pic = scipy.misc.ascent()
# plt.imshow(pic)
# plt.show()

# print(pic.dtype)  # int32
# print(pic.shape)  # (512,512)
#
xmax = pic.shape[0]
ymax = pic.shape[1]
# pic[range(xmax), range(ymax)] = 0  # 0 表示黑色
# plt.imshow(pic)
# plt.show()

# print(pic[0][0])
# print(pic[511][511])
for x in range(xmax):
    for y in range(ymax):
        print('x={},y={} color:{}'.format(x, y, pic[x][y]))
    break
