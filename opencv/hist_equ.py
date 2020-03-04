import cv2
import numpy as np

img = cv2.imread("/home/sub0811/Desktop/underwater_gate.jpeg")

print(type(img))

r, g, b = cv2.split(img)

cv2.imshow("og", img)

eq_r = cv2.equalizeHist(r)
eq_g = cv2.equalizeHist(g)
eq_b = cv2.equalizeHist(b)

eq = cv2.merge((eq_r, eq_g, eq_b))

cv2.imshow("er", eq_r)
cv2.imshow("eg", eq_g)
cv2.imshow("eb", eq_b)

cv2.imshow("og", img)
cv2.imshow("hist", eq)

cv2.waitKey()

