import numpy as np
import cv2

img = np.zeros((600, 600, 3), np.uint8)
img = cv2.rectangle(img, (200, 200), (400, 400), (200, 200, 200), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()