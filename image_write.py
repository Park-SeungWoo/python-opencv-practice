import cv2

img = cv2.imread('images/ltj.jpeg', 1)
gray = cv2.imread('images/ltj.jpeg', 0)
un = cv2.imread('images/ltj.jpeg', -1)

cv2.imshow('Imgae', img)

while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break
    elif k == ord('g'):
        cv2.imwrite('images/ltj_gray.jpg', gray)
        cv2.imshow('gray', gray)
    elif k == ord('u'):
        cv2.imwrite('images/ltj_unchanged.jpg', un)
        cv2.imshow('unchanged', un)

