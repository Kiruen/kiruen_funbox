import array
import numpy as np

import ctypes
print(ctypes.int)

print(np.ones((3,5), dtype=float))
print(np.full((30,50), 1.6))
arr = np.arange(0, 19, 3)
print(arr)

arr = np.linspace(0, 100, 20)
print(arr)

arr = np.random.random(100)
arr.shape = 25, 4
print(arr)

arr = np.random.normal(0, 1, (5, 5))
print(arr)

arr = np.eye(5)
print(arr)

arr = np.empty(30)
arr.shape = 5,6
print(arr)

arr = np.random.randint(10, size=(3,4,5), dtype=np.int64)
print(arr)
print(arr.ndim, arr.size, arr.dtype, arr.nbytes)

aspect = arr[0,1:3,:]
a = np.array([[1,1,1,1,1],[1,1,1,1,1]])
a.resize((2,5))
aspect[:] = a
print(arr)

aspect_copy = arr[0,:,0].copy()
aspect_copy[0] = 6666
print(arr)

import tempfile
with tempfile.TemporaryDirectory() as test_dir:
    print(test_dir)

def foo1():
    val = 123
    def clo():
        return val
    print(foo1.__closure__)

def foo():
    foo1()

# import pdb; pdb.set_trace()
# foo()