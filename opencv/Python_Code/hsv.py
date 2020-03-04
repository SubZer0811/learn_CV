import cv2
import numpy as np

def rgb(cap):

	ret, frame = cap.read()
	while(ret):

		frame = cv2.resize(frame, (960, 640))
		cv2.imshow("frame", frame)
		# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		b, g, r = cv2.split(frame)
		
		r += 200
		g.fill(100)
		b.fill(100)

		img = cv2.merge([b, g, r])
		cv2.imshow("mod", img)
		cv2.waitKey(10)
		ret, frame = cap.read()
		if cv2.waitKey(100) == 27:
			break
		
		if cv2.waitKey(10) & 0xFF == ord('p'):
			cv2.waitKey()




def hsv():
	while(ret):

		frame = cv2.resize(frame, (960, 480))
		cv2.imshow("frame", frame)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		h, s, v = cv2.split(hsv)
		# print(h.shape, s.shape, v.shape)
		# s += 50
		# h += 20
		hs = cv2.merge(h, s)
		# s.fill(255)
		# v.fill(127)
		hsv = cv2.merge([h, s, v])
		img = hsv
		# img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

		cv2.imshow("mod", img)
		cv2.waitKey(100)
		ret, frame = cap.read()
		if cv2.waitKey(10) == 27:
			break

def cmyk(cap):

	ret, frame = cap.read()
	while(ret):

		frame = cv2.resize(frame, (960, 640))
		c, m, y, k = cv2.split(cv2.cvtColor(frame, cv2.))


if __name__ == "__main__":
	
	cap = cv2.VideoCapture("/home/sub0811/Documents/Gate_Video/100GOPRO/m4v/10.mp4")

	ret, frame = cap.read()

	# img1 = cv2.imread("/home/sub0811/Documents/Gate_Video/100GOPRO/m4v/10/10_30.jpeg")
	# img2 = cv2.imread("/home/sub0811/Documents/Gate_Video/100GOPRO/m4v/10/10_370.jpeg")
	# img1 = cv2.resize(img1, (500, 500))
	# img2 = cv2.resize(img2, (500, 500))
	# cv2.imshow("1", img1)
	# cv2.imshow("2", img2)

	# cv2.waitKey()

	rgb(cap)
	