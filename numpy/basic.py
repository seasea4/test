import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

print(a.flags)

print("dimension" , a.ndim)
print("要素数", a.size)
print("shape", a.shape)
print("要素のデータ型", a.dtype)
