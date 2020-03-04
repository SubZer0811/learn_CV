import cv2
import numpy as np

img = cv2.imread("gate_1.jpeg")
roi = img[50:1000, 50:1000]

cv2.imshow("roi", roi)
cv2.waitKey()