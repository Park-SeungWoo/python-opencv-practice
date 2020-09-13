import cv2

img_color = cv2.imread('images/myphoto.jpeg', cv2.IMREAD_COLOR)

cv2.imshow('Show image', img_color)

cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('Show converted gray image', img_gray)
cv2.waitKey(0)

cv2.imwrite('images/cvtimg.jpg', img_gray)

cv2.destroyAllWindows()