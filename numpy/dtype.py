'''
配列要素のデータ型は
numpy.dtype
というオブジェクトで扱われる。
５つの型があり、
bool
signed int
unsigned int
float
complex

URL: https://docs.scipy.org/doc/numpy/user/basics.types.html
'''

import numpy as np

a = np.array([1,2,3,4,5])
print(a.dtype)
print(a.itemsize)

b = np.array([1.0, 2.0, 3.0, 4.0])
print(b.dtype)

c = np.array([1,2,3,4,5], dtype=np.int32)
print(c.dtype)
print(c.itemsize)

d = np.array([1,2,3], dtype=np.uint8)
print(d.dtype)
print(d.itemsize)
