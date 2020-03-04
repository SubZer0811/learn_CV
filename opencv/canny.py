import cv2
import numpy as np 
import matplotlib.pyplot as plt 

# img = cv2.cvtColor(cv2.imread("/home/sub0811/Desktop/test.png"),cv2.COLOR_BGR2RGB)

# img = cv2.imread("/home/sub0811/Desktop/test.png")


cap = cv2.VideoCapture("/home/sub0811/Documents/Gate_Video/underwater_comp/3_comp.avi")

while(True):
	
	ret, img = cap.read()
	img = cv2.resize(img, (960, 540))

	img = cv2.GaussianBlur(img,(5, 5), 10)
	img = cv2.GaussianBlur(img,(5, 5), 10)
	img = cv2.GaussianBlur(img,(5, 5), 10)
	# img = cv2.GaussianBlur(img,(5, 5), 10)
	img = cv2.erode(img, (5, 5))

	cv2.imshow("color", img)
	xedge = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
	yedge = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

	abs_x = cv2.convertScaleAbs(xedge)
	abs_y = cv2.convertScaleAbs(yedge)
	
	grad = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
	
	# edge = cv2.Canny(img,10,10)

	# if(cv2.waitKey(10) == "q")
	# 	break

	cv2.imshow('frame',grad)
	cv2.waitKey(1)





