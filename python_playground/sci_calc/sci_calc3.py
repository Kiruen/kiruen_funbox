import numpy as np
import matplotlib.pyplot as plt

# 最近邻
X = np.random.rand(10, 2)  # 2个维度，10个点，范围0,1
print(X, X.shape)

# import seaborn; seaborn.set() # 设置画图风格
# plt.scatter(X[:, 0], X[:, 1], s=100)
# plt.show()

print(X[:, np.newaxis, :] - X[:, :, np.newaxis])

people_data = np.zeros(4, {'names': ('name', 'age', 'weight'),
                           'formats': ('U10', 'i4', 'f8')})
print(people_data)
print(people_data.dtype)
people_data[0]['name'] = 'kiruen'
print(people_data['name'])
print(people_data[people_data['name'] != ''])

print( np.dtype([('name', np.str_)]) )