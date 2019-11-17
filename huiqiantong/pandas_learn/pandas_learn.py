import re

import numpy as np
import pandas as pd

df = pd.read_csv(r'results.csv')
# print(df.head(10))
# print(df.shape)
# print(df.shape)
# print(df.head(10))
# print(df.head(0))
# print("*"*50)
# print(df.iloc[0])
# print(df.iloc[0, 2])
# print(df.iloc[0:3, 2])
# df.set_index()
df.set_index('id', inplace=True)  # id不再是数据，而是变为了索引
# print(df.head(10))
# print(df)
# print(df.loc[2, 'a']) #  重新设置了索引不能用iloc了而是loc
# print(df.loc[3, 'data'])
# df.drop(['b'], axis=1, inplace=True)   # 把b这个列删除  axis默认为0表示行 1表示列
# print(df)
# df.drop(columns=['c'], inplace=True)  # 删除c列
# df.drop(index=)   行
df.drop(columns=['d', 'e', 'f'], inplace=True)
# print(df)
columns = df.columns
# print(columns)
df.columns = ['A', 'B', "C", "D", 'E', 'F', 'G']


# print(df.columns)
# print(df)
# print(df['A'])
# print(df.A)
def get_date(date):
    date = str(date)
    # print('_get_Date_Fun')
    regex = r'^(\d{4})'  # 正则表达式
    res = re.search(regex, date)
    # print(type(res.group()))
    # print((res.group(1)))
    if res:
        return (res.group(1))
    else:
        return np.NaN


df.A = df['A'].map(get_date)  # get_date为函数   用map应用于函数

# print(df)
df.C = df['C'].fillna('1886')  # 填充数据  为空的NaN 替换为设置的值
print(df)
# df.groupby()
# df1 = df.sample(2)   # 随机取数据 取样
# print(df1)
# df1.to_csv('new_result.csv')
