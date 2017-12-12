import numpy as np
import cv2
from random import randint

cols, rows = 640, 480

# numpyを用いた画像の生成

img = np.zeros((rows, cols, 3), np.uint8)
#cv2.imshow("TEST", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# itemsetを用いた画素値の変更
targetc = randint(0, 640)
targetr = randint(0, 480)

r = randint(0, 256)
g = randint(0, 256)
b = randint(0, 256)

img.itemset((targetr, targetc, 0), r)
img.itemset((targetr, targetc, 0), g)
img.itemset((targetr, targetc, 0), b)

#cv2.imshow("TEST", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# 配列的アクセス

img[targetr, targetc] = [b, g, r]
img[0:240, 0:320] = [128, 0, 0]

cv2.imshow("TEST", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
