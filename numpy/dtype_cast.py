'''
ndrarray.astype()
'''

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a.dtype)

a = a.astype(np.int32)
print(a.dtype)
