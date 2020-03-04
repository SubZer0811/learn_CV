import cv2
import numpy as np
import os

def avg(img1, img2):

	img = np.add(img1, img2)
	img = np.divide(img, 2)
	return img

if __name__ == "__main__":

	directory = '/home/sub0811/Documents/Gate_Video/100GOPRO/m4v/background'
	
	i = 1
	images = []

	gate = cv2.imread("/home/sub0811/Documents/Gate_Video/100GOPRO/m4v/10/10_355.jpeg")
	gate = cv2.resize(gate, (500, 500))
	cv2.imshow("gate", gate)
	for filename in os.listdir(directory):
		
		filename = directory + "/" + filename
		images.append(filename)

	print(images[0])
	# img1 = cv2.imread(images[0])
	# img2 = cv2.imread(images[1])
	avg = cv2.imread(images[0])
	avg = cv2.resize(avg, (500, 500))
	for i in range(1, len(images)):
		print(i)
		img = cv2.imread(images[i])
		img = cv2.resize(img, (500, 500))
		avg += img
		avg = avg/2
		cv2.imshow("avg", avg)

		cv2.imwrite("bg_" + str(i) + ".jpeg", avg)
		sub = np.subtract(gate, avg)
		sub = np.array(sub)
		cv2.imshow("sub", sub)
		# img2 = cv2.imread(images[1])
		# img1 = avg(img1, img2)
	
	avg = np.array(avg)
	# avg = avg.astype(int)
	print(avg)
	cv2.imshow("pic", avg)
	cv2.waitKey()