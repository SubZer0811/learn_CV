import cv2
import numpy as np
from gen_bg_sub import avg_kern

# img = cv2.imread("avg_gate.jpeg")
# for i in range(0, 255):
# 	for j in range(0, 255):
# 		print(i, j)
# 		edged = cv2.Canny(img, i, 255)
# 		cv2.imshow("thresh", edged)

# 		# if(cv2.waitKey(100) == 'q'):
# 		# 	break
# 	cv2.waitKey(1)

cap = cv2.VideoCapture("/home/sub0811/Documents/Gate_Video/100GOPRO/m4v/8.mp4")

ret, frame = cap.read()
# cv2.imshow("frame", frame)
while(ret):
	
	frame = cv2.resize(frame, (200, 200))
	cv2.imshow("frame", frame)
	avg = avg_kern(frame, (2, 2))
	cv2.imshow("avg", avg)

	thresh = cv2.adaptiveThreshold(cv2.cvtColor(avg, cv2.COLOR_BGR2GRAY), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 1)
	cv2.imshow("thresh", thresh)
	ret, frame = cap.read()
	ret, frame = cap.read()
	ret, frame = cap.read()
	ret, frame = cap.read()
	ret, frame = cap.read()
	ret, frame = cap.read()
	cv2.waitKey(1)

cv2.waitKey()