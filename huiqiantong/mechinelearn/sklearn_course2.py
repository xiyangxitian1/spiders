from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import accuracy_score

sample_data = datasets.load_digits()

train_data, test_data, train_target, test_target = train_test_split(
    sample_data.data,
    sample_data.target)

# knn模型。默认为5个  创建一个模型，这就是建模了，这就是封装好的算法
# 以后加深可以看下是怎么写的源码
knn_model = KNeighborsClassifier(n_neighbors=8)

knn_model.fit(train_data, train_target)
pred = knn_model.predict(test_data)
print(pred[:10])
print(test_target[:10])

acc = accuracy_score(pred, test_target)
print(acc)
