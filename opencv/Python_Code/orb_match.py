import cv2
import numpy as np
from matplotlib import pyplot as plt

orb = cv2.ORB_create()

eraser = cv2.imread("/home/sub0811/Desktop/opencv/motion/gate_1.jpeg")
scene = cv2.imread("/home/sub0811/Desktop/opencv/motion/gate_2.jpeg")

#print(eraser.shape)
w = eraser.shape[0]
h = eraser.shape[1]

kp1, des1 = orb.detectAndCompute(eraser, None)
kp2, des2 = orb.detectAndCompute(scene, None)

bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, True)

matches = bf.match(des1, des2)

matches = sorted(matches, key = lambda x: x.distance)
good_matches = matches[:10]

src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches     ]).reshape(-1,1,2)
dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ]).reshape(-1,1,2)

M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
matchesMask = mask.ravel().tolist()
h,w = eraser.shape[:2]
pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)

dst = cv2.perspectiveTransform(pts,M)
dst += (w, 0)  # adding offset

draw_params = dict(matchColor = (0,255,0), # draw matches in green color
               singlePointColor = None,
               matchesMask = matchesMask, # draw only inliers
               flags = 2)

img3 = cv2.drawMatches(eraser,kp1,scene,kp2,good_matches, None,**draw_params)

# Draw bounding box in Red
img3 = cv2.polylines(img3, [np.int32(dst)], True, (0,0,255),3, cv2.LINE_AA)

cv2.imshow("result", img3)
cv2.waitKey()