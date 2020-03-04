import cv2
import numpy as np

img = cv2.imread("/home/sub0811/Desktop/opencv/images/gate.jpg")
cv2.imshow("org", img)

# test = img
test = np.copy(img)
w = test.shape[0]
h = test.shape[1]
print(w, h)

ha = int(w/2)

for i in range(int(w)):
	for j in range(h):
		test[i][j][0] -= 50
		test[i][j][1] += 50
		test[i][j][2] = test[i][j][2] + 127


cv2.imshow("org", img)
cv2.imshow("!blue", test)


cv2.waitKey()