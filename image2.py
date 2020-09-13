import cv2

img_gray = cv2.imread('images/ltj.jpeg', cv2.IMREAD_COLOR)
img_color = cv2.cvtColor(img_gray, cv2.COLOR_BGR2RGB)

cv2.imshow('Gray', img_gray)

cv2.waitKey(0)

cv2.imshow('color', img_color)

cv2.waitKey(0)

cv2.destroyAllWindows()