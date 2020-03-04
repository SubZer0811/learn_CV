import cv2
import numpy as np

cap = cv2.VideoCapture('/home/sub0811/Desktop/opencv/Gate_Video/1.mp4')

while(cap.isOpened()):
	
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	_, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)

	image, contours, hierarchy =  cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(image,contours,-1,(0,255,0))
	cv2.imshow('draw contours',image)

	cv2.waitKey(5)

imshow("frame", img)

cv2.destroyAllWindows()
cap.release()