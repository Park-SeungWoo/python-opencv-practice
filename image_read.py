import cv2

img = cv2.imread('images/ltj.jpeg', cv2.IMREAD_COLOR)
gray = cv2.imread('images/ltj.jpeg', 0)
unch = cv2.imread('images/ltj.jpeg', -1)

cv2.imshow('Unchanged', unch)
cv2.imshow('Gray', gray)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()