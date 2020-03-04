import cv2
import numpy as np

def avg_colour(img):

	b, g, r = 0, 0, 0
	for i in range(w):
		for j in range(h):
			b += img[i][j][0]
			g += img[i][j][1]
			r += img[i][j][2]
	
	return b/total_pixel, g/total_pixel, r/total_pixel

def bg_subtract(frame, bg):


	img = frame
	for i in range(w):
		for j in range(h):
			
			if( img[i][j][0] - bg[0] < 0 ):
				print("test")
				img[i][j][0] = 255
			else:
				img[i][j][0] -= bg[0]
			if( img[i][j][1] - bg[1] < 0 ):
				print("test")
				img[i][j][1] = 255
			else:
				img[i][j][1] -= bg[1]
			if( img[i][j][2] - bg[2] < 0 ):
				print("test")
				img[i][j][2] = 255
			else:
				img[i][j][2] -= bg[2]

	return img



org = cv2.imread("/home/sub0811/Desktop/practice/opencv/underwater_gate.jpeg")		#10, 150, 160
org = cv2.resize(org, (200, 200))

w = org.shape[0]
h = org.shape[1]
total_pixel = w*h

gate = cv2.GaussianBlur(org, (11, 11), 10)

cv2.imshow("Original", gate)

avg = np.array(avg_colour(gate))
avg = avg.astype(int)

bg_sub = bg_subtract(gate, avg)

cv2.imshow("bg_sub", bg_sub)
cv2.imwrite("bg_sub.jpeg", bg_sub)

# thresh = cv2.threshold(bg,)

# print(avg)
# print(gate[0][0])

cv2.waitKey()