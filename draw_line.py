import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
img = cv2.line(img, (0, 0), (511, 511), (200, 100, 100), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()