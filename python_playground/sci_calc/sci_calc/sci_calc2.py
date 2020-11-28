import numpy as np
arr = np.arange(1, 10).reshape((3, 3))
print(arr)
line = arr[0]
print(line.reshape(1,3))
print(line[np.newaxis, :])

print(np.concatenate([arr[1], [22,22,22], (3, 3, 3)]))
print(np.concatenate([arr, np.arange(11, 20).reshape((3,3))]))

print(np.vstack([arr, arr]))
print(np.hstack([arr, arr]))

l = np.random.randint(1,100, size=20) # list(range(1, 21))
arr = np.empty(len(l))
for i in range(20):
    arr[i] = 1 / l[i]
print(arr)

print(1 / l)

print(abs(np.array([1+2j, .2+4.6j, 3j, 1j, 7])))

x = np.arange(5)
y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)

arr = np.arange(1, 10)
print(np.multiply.outer(arr, arr))

arr = np.random.rand(10000)
print(np.sum(arr))

arr = np.random.random((50, 50))
print(arr.sum())
print(arr.min(axis=0))

arr = np.random.random((5, 5))
print(arr + [1,1,1,1,1] + 2)

a = np.arange(3)
print(a, a.shape)
print(a[:, np.newaxis])

# 归一化
arr = np.random.random((10, 3))
arr_mean = arr.mean(axis=0)
print(arr_mean)
print(arr.mean(1))

arr_centered = arr - arr_mean
print(arr_centered)
print(arr_centered.mean(0))  # 全部接近于0

# 使用广播绘制二元函数图像
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
z = np.sin(x) ** 10 + np.cos(10 + x * y) * np.cos(x)

import matplotlib.pyplot as plt
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5],
                   cmap='viridis')
plt.colorbar()
# plt.show()


x = np.random.randint(10, size=(3, 4))
print("x:", x)
print(np.count_nonzero(x < 3, axis=1))

print((x < 3) & (x >1))

x = np.arange(1, 100)
# print(x[[[1,2],[11,12]]])
print(x[np.array([[1,2],[11,12]])])

x = np.arange(0, 56).reshape((8, 7))
row = np.array([0, 2, 4])
col = np.array([5, 3, 1])
print(x)
print(x[row, col])
print(x[row[:, np.newaxis], col])
print(x[:, 5:7])
print(x[:, np.array([0,0,0,0,1,0,1], dtype=bool)])

x = np.arange(1, 11)
i = [1,2,2,3,3]
np.add.at(x, i, 2)
print(x)

x = np.random.randn(100)
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)
np.add.at(counts, np.searchsorted(bins, x), 1)
print(counts)

si = np.argsort(counts)
print(counts[si])
print(counts[si] == np.sort(counts))

x = np.random.randint(1, 43, (6, 7))
print(x)
print(np.sort(x), np.sort(x, axis=1))

print(np.partition(x[1], 3))
print(np.partition(x, 3, axis=1))
si = np.argpartition(x, 3, axis=1)
print("按照行重新装配：", x[[1,2,3,4,5,0]])
print("展示第一行：", x[0, si[0]])
# print("展示全部：", x[:, si])
print("展示全部：", np.array([x[i, si[i]] for i in range(x.shape[0])]))  # 有无更好的办法？