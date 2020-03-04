import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("balls.jpeg")
#print(img)
cv2.imshow("img", img)

print(img.shape)
w = img.shape[0]
h = img.shape[1]

orb = cv2.ORB_create()

kp = orb.detect(img, None)

kp, des = orb.compute(img, kp)

dest = np.empty((w, h))

img2 = cv2.drawKeypoints(img, kp, outImage = dest, color = (0, 255, 0), flags = 0)

plt.imshow(img2), plt.show()
cv2.waitKey(0)