'''
配列要素の参照/代入、スライスについて
基本はリストだから、付属品を覚えるだけ
'''

import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[2])
print(a[1][2])
print(a[1,2])
