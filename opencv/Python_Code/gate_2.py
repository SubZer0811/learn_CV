import cv2
import numpy as np
from gen_bg_sub import avg_kern

org = cv2.imread("/home/sub0811/Desktop/practice/opencv/underwater_gate.jpeg")
org = cv2.resize(org, (300, 300))
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

cv2.imshow("original_gray", gray)


avg = avg_kern(org, (2, 2))
cv2.imshow("iter1", avg)
avg = avg_kern(avg, (2, 2))
cv2.imshow("iter2", avg)

cv2.imwrite("avg_gate.jpeg", avg)
avg_gray = cv2.cvtColor(avg, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", avg_gray)
edged = cv2.Canny(avg, 50, 80)

cv2.imshow("edged", edged)

cv2.waitKey()