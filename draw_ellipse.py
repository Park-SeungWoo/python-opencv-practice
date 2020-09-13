import numpy as np
import cv2

img = np.zeros((600, 600, 3), np.uint8)
img = cv2.ellipse(img, (300, 300), (100, 50), 0, 0, 360, (200, 100, 100), -1)

img = cv2.ellipse(img, (300, 300), (50, 25), 0, 0, 360, (0, 0, 0), -1)
#300,300은 가운데 좌표, 50,25는 가장 먼 점까지와 가까운점까지의 길이 그다음 세 숫자는 타원 기울기, 시작점 기울기, 끝점 기울기임
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()