import numpy as np
import cv2

img = np.zeros((600, 600, 3), np.uint8)
img = cv2.circle(img, (300, 300), 100, (100, 100, 200), 2)

img = cv2.circle(img, (300, 300), 50, (100, 200, 100), -1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyALlWindows()