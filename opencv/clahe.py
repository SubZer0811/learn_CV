import cv2
import numpy as np

img = cv2.imread("/home/sub0811/Desktop/underwater_gate.jpeg")

img = cv2.GaussianBlur(img, (11, 11), 10)

lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

spl_lab_img = cv2.split(lab_img)

cl = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

spl_lab_img[0] = cl.apply(spl_lab_img[0])
spl_lab_img[0] = cl.apply(spl_lab_img[0])
spl_lab_img[0] = cl.apply(spl_lab_img[0])

merge = cv2.merge((spl_lab_img[0], spl_lab_img[1], spl_lab_img[2]))

bgr = cv2.cvtColor(merge, cv2.COLOR_LAB2BGR)

cv2.imshow("og", img)
cv2.imshow("clahe", bgr)

cv2.waitKey()