import numpy as np
import cv2

img = np.zeros((640, 640, 3), np.uint8)
cv2.putText(img, 'Park Seung Woo', (10, 500), cv2.FONT_HERSHEY_COMPLEX, 2, (100, 200, 100), 2)

cv2.imshow('text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()