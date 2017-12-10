'''
よく使われるものを抑える
'''

import numpy as np

print( np.array([1,2,3]) )

# zeros and ones

print( np.zeros(5) )
print( np.ones(3) )

# 単位行列(identity)
print( np.identity(5) )

# range array
print( np.arange(10) )

# 反復配列
print(np.tile([2,4,5], 2))


# Deep copy
a = np.array([1, 2, 3], dtype=np.int32)
b = a.copy()

print(a)
print(b)
print(a==b)

# random array
print(np.random.randint(0, 100, 10))
