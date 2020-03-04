import cv2
import numpy as np
from matplotlib import pyplot as plt

orb = cv2.ORB_create()

eraser = cv2.imread("bottle_1.jpeg")
scene = cv2.imread("bottle_scene_2.jpeg")

#print(eraser.shape)
w = eraser.shape[0]
h = eraser.shape[1]

kp1, des1 = orb.detectAndCompute(eraser, None)
kp2, des2 = orb.detectAndCompute(scene, None)

bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, True)

matches = bf.match(des1, des2)



matches = sorted(matches, key = lambda x: x.distance)

out = np.empty((w, h))

img3 = cv2.drawMatches(eraser, kp1, scene, kp2, matches[:30], outImg = out, flags = 2)
plt.imshow(img3), plt.show()
cv2.waitKey(0)