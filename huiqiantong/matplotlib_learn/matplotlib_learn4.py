import matplotlib.pyplot as plt

# 子图   subplots可以设置子图之间的间距等
# plt.subplots()  
plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [3, 4, 5])
plt.subplot(2, 2, 2)
plt.scatter([1, 2, 3], [3, 6, 8])
# plt.subplot(2,2,3)
plt.subplot(2, 2, 4)
plt.plot([1, 2, 3], [5, 6, 7])
plt.show()
