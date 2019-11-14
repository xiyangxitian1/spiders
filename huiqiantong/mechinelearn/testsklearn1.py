from sklearn.externals import joblib
# from sklearn.linear_model import LinearRegression
import numpy as np

mymodel_t = joblib.load('houses.pkl')
x = [140, 145]
x = np.array(x).reshape(-1, 1)
pred = mymodel_t.predict(x)
print(pred)
