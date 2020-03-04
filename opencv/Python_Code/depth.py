import cv2
import numpy as np

def max_cont(conts):

	max = 0
	for i in conts:
		if cv2.contourArea(conts[max]) < cv2.contourArea(conts[i]):
			max = i

	return max 

if __name__ == "__main__":
	

	cap = cv2.VideoCapture(0)
	ret, frame = cap.read()
	print(frame.shape)
	while(ret):

		ret, frame = cap.read()
		grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		hsv = cv2.resize(hsv, (640, 480))
		
		# cv2.imshow("frame", grey)
		blur = cv2.GaussianBlur(hsv, (11, 11), 11)
		
		thresh = cv2.inRange(blur, np.array([34, 75, 92]), np.array([45, 255, 255]))
		dilate = cv2.dilate(thresh, None, iterations=3)
		erode = cv2.erode(dilate, None, iterations=3)
		# cv2.imshow("erode", erode)
	
		
		cv2.imshow("thresh", erode)

		_, contours, h = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
		# print(contours)
		if len(contours) != 0 :
			obj = max(contours, key=cv2.contourArea)
			# obj_idx = max_cont(contours)
		
		x, y, w, h = cv2.boundingRect(obj)
		img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0))
		cv2.imshow("track", img)

		# print(w)
		depth1 = 154 * 30 / w
		depth2 = 154 * 30 / h
		
		depth = (depth1 + depth2)/2
		print(depth)

		cv2.waitKey(10)