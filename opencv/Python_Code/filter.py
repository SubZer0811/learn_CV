import cv2
import numpy as np
from scipy.interpolate import UnivariateSpline


def rgb_filter(img):
	# img = cv2.GaussianBlur(img, (11, 11), 5)
	img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
	r_lut_in = [0, 60, 195]
	r_lut_out = [0, 133, 20]

	g_lut_in = [0, 66, 155, 213, 255]
	g_lut_out = [0, 0, 171, 100, 255]

	b_lut_in = [0, 64, 90, 132, 180, 255]
	b_lut_out = [0, 32, 64, 127, 191, 255]

	r_lut = np.interp(np.arange(0, 256), r_lut_in, r_lut_out).astype(np.uint8)
	g_lut = np.interp(np.arange(0, 256), g_lut_in, g_lut_out).astype(np.uint8)
	b_lut = np.interp(np.arange(0, 256), b_lut_in, b_lut_out).astype(np.uint8)

	b, g, r = cv2.split(img)

	r_new = cv2.LUT(r, r_lut)
	g_new = cv2.LUT(g, g_lut)
	b_new = cv2.LUT(b, b_lut)

	mod = cv2.merge([b_new, g_new, r_new])

	cv2.imshow("org", img)
	cv2.imshow("mod", mod)
	cv2.waitKey(10)


def hsv_filter(img):
	# img = cv2.GaussianBlur(img, (11, 11), 5)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
	h_lut_in = [0, 21, 40, 255]
	h_lut_out = [255, 70, 100, 255]

	s_lut_in = [0, 110, 255]
	s_lut_out = [0, 255, 255]

	v_lut_in = [0, 110, 255]
	v_lut_out = [0, 110, 255]

	h_lut = np.interp(np.arange(0, 256), h_lut_in, h_lut_out).astype(np.uint8)
	s_lut = np.interp(np.arange(0, 256), s_lut_in, s_lut_out).astype(np.uint8)
	v_lut = np.interp(np.arange(0, 256), v_lut_in, v_lut_out).astype(np.uint8)

	h, s, v = cv2.split(img)

	h_new = cv2.LUT(h, h_lut)
	s_new = cv2.LUT(s, s_lut)
	v_new = cv2.LUT(v, v_lut)

	mod = cv2.merge([h, s_new, v_new])
	mod = cv2.cvtColor(mod, cv2.COLOR_HSV2BGR)
	img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
	cv2.imshow("org", img)
	cv2.imshow("mod", mod)
	cv2.waitKey(10)



# img = cv2.GaussianBlur(img, (11, 11), 10)


if __name__ == "__main__":
	
	# img = cv2.imread("/home/sub0811/Documents/Gate_Video/25_01_2020/m4v/13/13_521.jpeg")
	# # img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

	# rgb_filter(img)
	# cv2.waitKey()

	i = 10
	while(i<=10):
		cap = cv2.VideoCapture("/home/sub0811/Documents/Gate_Video/25_01_2020/m4v/original_m4v/" + str(i) + ".m4v")

		ret, frame = cap.read()

		while(ret):
			rgb_filter(frame)
			ret, frame = cap.read()	

		i += 1