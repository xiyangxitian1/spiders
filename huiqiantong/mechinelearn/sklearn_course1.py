import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

# 1.准备数据
x, y = make_regression(n_samples=100, n_features=1, noise=10)

# plt.scatter(x, y)
#
# plt.show()

# 2.建模
model = LinearRegression()

# 3.训练
# print(x)
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
model.fit(x, y)

# train_code = model.score(x, y)
# print(train_code)

new_houses = [125, 130]
new_houses = np.array(new_houses).reshape(-1, 1)
pred = model.predict(new_houses)
print(pred)
joblib.dump(model, 'houses.pkl')

mymodel_t = joblib.load('houses.pkl')
x = [140, 145]
x = np.array(x).reshape(-1, 1)
pred = mymodel_t.predict(x)