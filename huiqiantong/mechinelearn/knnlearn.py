import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1.加载数据
simple_data = datasets.load_digits()
# print(len(simple_data.data)) # 1797条数据
# print(len(simple_data))
# img1 = simple_data.images[1]
# print(img1)

# target1 = simple_data.target[1]
# print(target1)

# plt.matshow(img1)
# plt.imshow(img1)
# plt.show()  # 显示出图片
# data1 = simple_data.data[1]  # 64长度的列表

# print(data1)
train_data, test_data, train_target, test_target = train_test_split(
    simple_data.data, simple_data.target,
    test_size=0.2)
# print(len(train_data))
# 建模
knn_model = KNeighborsClassifier(n_neighbors=5)

# 训练模型
knn_model.fit(train_data, train_target)

# 预测结果
pred = knn_model.predict(test_data)
print(pred[:10])
# 实际结果
print(test_target[:10])

acc = accuracy_score(pred, test_target)
print('准确度：', acc)

