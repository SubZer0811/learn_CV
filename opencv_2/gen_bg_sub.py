import cv2
import numpy as np

def avg_kern(img, ksize):

	h = img.shape[0]
	w = img.shape[1]

	dest = np.zeros((h-ksize[0], w-ksize[1], 3), dtype = int)
	karea = ksize[0] * ksize[1]
	print(ksize)
	i, j = 0, 0
	for i in range(w-ksize[0]):
		for j in range(h-ksize[1]):
			# print(i, j)

			for x in range(i, i+ksize[0]):
				for y in range(j, j+ksize[1]):
					
					dest[i][j][0] += img[x][y][0]
					dest[i][j][1] += img[x][y][1]
					dest[i][j][2] += img[x][y][2]

					y += 1
				x += 1

			j += ksize[0]
		i += ksize[1]
	
	dest = np.array(dest).astype(np.uint8)

	return dest


if __name__ == "__main__":


	img = cv2.imread("/home/sub0811/Desktop/practice/opencv/underwater_gate.jpeg")
	cv2.imshow("original", img)
	img = cv2.resize(img, (300, 300))

	# dest = np.array(avg_kern(img, (2, 2)))
	# dest = dest.astype(np.uint8)
	dest = avg_kern(img, (2, 2))
	cv2.imshow("kernel size 2", dest)

	cv2.waitKey()