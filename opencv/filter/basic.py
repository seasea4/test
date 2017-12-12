import numpy as np
import cv2

img = cv2.imread("sample.jpg", 0)

# more bright

white_kernel = np.ones((img.shape[0], img.shape[1]), dtype=np.uint8) * 255
img = cv2.addWeighted(img, 0.8, white_kernel, 0.2, 0)

# smoothing filter
kernel1 =  np.ones(5, np.float32) / 25
dst = cv2.filter2D(img, -1, kernel1)

dst = cv2.addWeighted(dst, 0.8, white_kernel, 0.2, 0)
res = np.vstack((img, dst))

cv2.imshow("test", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
