import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/ltj.jpeg', 1)

b, g, r = cv2.split(img)
img = cv2.merge([r, g, b])

plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()
