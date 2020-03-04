import cv2
import numpy as np
from gen_bg_sub import avg_kern

cap = cv2.VideoCapture("/home/sub0811/Documents/Gate_Video/100GOPRO/m4v/6.mp4")

ret1, frame1 = cap.read()
frame1 = cv2.resize(frame1, (500, 500))
ret2, frame2 = cap.read()
frame2 = cv2.resize(frame2, (500, 500))

while(ret2):

	diff = cv2.absdiff(frame1, frame2)
	frame1 = frame2
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	ret2, frame2 = cap.read()
	frame2 = cv2.resize(frame2, (500, 500))
	cv2.imshow("diff", diff)
	cv2.waitKey(10)