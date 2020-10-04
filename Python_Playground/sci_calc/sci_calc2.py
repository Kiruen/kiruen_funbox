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