import array, random as ran
arr = array.array('d', (ran.random() for i in range(10**3)))
print(len(arr))

with open('nums.txt', 'wb') as fp:
    arr.tofile(fp)
print(arr[-1])

arr2 = array.array('d')

with open('nums.txt', 'rb') as fp:
    arr2.fromfile(fp, len(arr))
    print(arr2[-1])
    print(arr == arr2, arr is arr2)

arr3 = array.array('h', [1, -1, 2, 0, -2]) # 00 01 11 11 00 02 11 1e 这个是大端法
view = memoryview(arr3)
print(view[-2])
view_oct = view.cast('B')
print(view_oct.tolist()) # 一看，是小端法表示
view_oct[4] = 4 #修改了byte3的低字节， 00 02 变成了 00 04
print(arr3)

import numpy as np
arr4 = np.arange(1, 121)
print(arr4)
print(type(arr4), arr4.shape)
arr4.shape = 10,12
print(arr4[2], arr4[2, 3])
print(arr4.transpose() * 6)
print("输出第三列：", arr4[:, 3])

import collections as coll
dque = coll.deque(range(10), maxlen=10)
dque.rotate(3)  # 循环右移
print(dque)
dque.appendleft(-1)
print(dque)
dque.extend([1,9,9,7])
print(dque)
