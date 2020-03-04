import cv2
import numpy as np

def nothing(x):
	pass

if __name__ == "__main__":
	
	img = cv2.imread("/home/sub0811/Documents/Gate_Video/100GOPRO/m4v/10/10_219.jpeg")
	img = cv2.resize(img, (960, 640))
	cv2.namedWindow("hsv_trackbar")
	# cv2.imshow("hsv_trackbar",img)
	cv2.createTrackbar('h',"hsv_trackbar", 0, 255, nothing)
	cv2.createTrackbar('s',"hsv_trackbar", 0, 255, nothing)
	cv2.createTrackbar('v',"hsv_trackbar", 0, 255, nothing)

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	while(1):

		h, s, v = cv2.split(hsv)

		h_val = cv2.getTrackbarPos('h',"hsv_trackbar")
		s_val = cv2.getTrackbarPos('s',"hsv_trackbar")
		v_val = cv2.getTrackbarPos('v',"hsv_trackbar")

		h += h_val
		s += s_val
		v += v_val

		hsv = cv2.merge([h, s, v])
		cv2.imshow("hsv_trackbar", cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR))
		cv2.waitKey(10000)

		if(cv2.waitKey(10) == ord('q')):
			break




# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# def nothing(x):
#   pass
# cv2.namedWindow('Colorbars')
# hh='Max'
# hl='Min'
# wnd = 'Colorbars'
# cv2.createTrackbar("Max", "Colorbars",0,255,nothing)
# cv2.createTrackbar("Min", "Colorbars",0,255,nothing)
# img = cv2.imread("/home/sub0811/Documents/Gate_Video/100GOPRO/m4v/10/10_219.jpeg",0)
# img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# # titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# # images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# # for i in xrange(6):
# #     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
# #     plt.title(titles[i])
# #     plt.xticks([]),plt.yticks([])
# # plt.show()
# while(1):
#    hul=cv2.getTrackbarPos("Max", "Colorbars")
#    huh=cv2.getTrackbarPos("Min", "Colorbars")
#    ret,thresh1 = cv2.threshold(img,hul,huh,cv2.THRESH_BINARY)
#    ret,thresh2 = cv2.threshold(img,hul,huh,cv2.THRESH_BINARY_INV)
#    ret,thresh3 = cv2.threshold(img,hul,huh,cv2.THRESH_TRUNC)
#    ret,thresh4 = cv2.threshold(img,hul,huh,cv2.THRESH_TOZERO)
#    ret,thresh5 = cv2.threshold(img,hul,huh,cv2.THRESH_TOZERO_INV)
#    # cv2.imshow(wnd)
#    cv2.imshow("thresh1",thresh1)
#    cv2.imshow("thresh2",thresh2)
#    cv2.imshow("thresh3",thresh3)
#    cv2.imshow("thresh4",thresh4)
#    cv2.imshow("thresh5",thresh5)
#    k = cv2.waitKey(1) & 0xFF
#    if k == ord('m'):
#      mode = not mode
#    elif k == 27:
#      break
# cv2.destroyAllWindows()