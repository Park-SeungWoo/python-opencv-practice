import numpy as np
import cv2

img = np.zeros((640, 640, 3), np.uint8)
pts = np.array([[315, 160], [150, 280], [210, 480], [420, 480], [480, 280]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (100, 200, 100), 3)

cv2.imshow('poly', img)
cv2.waitKey(0)
cv2.destroyAllWindows()