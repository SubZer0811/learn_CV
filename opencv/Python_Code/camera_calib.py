import cv2
import numpy as np
import glob


def Take_Pic():

	cap = cv2.VideoCapture(0)
	ret, frame = cap.read()
	i = 34
	while(ret):

		ret, frame = cap.read()
		cv2.imshow("frame", frame)
		if cv2.waitKey(10) == 27:
			cv2.imwrite(str(i) + ".jpeg", frame)
			i += 1

		if cv2.waitKey(10) == 65:
			break

	

def calib():
	# termination criteria
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

	# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
	objp = np.zeros((9*6,3), np.float32)
	objp[:,:2] = np.mgrid[0:6,0:9].T.reshape(-1,2)

	# Arrays to store object points and image points from all the images.
	objpoints = [] # 3d point in real world space
	imgpoints = [] # 2d points in image plane.

	images = glob.glob('*.jpeg')
	
	for fname in images:
		img = cv2.imread(fname)
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		# print(fname)
		# Find the chess board corners
		ret, corners = cv2.findChessboardCorners(gray, (9,6),None)
		# print(ret, corners)
		# If found, add object points, image points (after refining them)
		if ret == True:
			objpoints.append(objp)
			print("test")
			corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
			imgpoints.append(corners2)

			# Draw and display the corners
			img = cv2.drawChessboardCorners(img, (9,6), corners2,ret)
			cv2.imshow('img',img)
			cv2.waitKey(0)

	ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
	print(mtx)
	
	
	img = cv2.imread('10.jpeg')
	h,  w = img.shape[:2]
	print(h, w)
	# newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
	
	undist = cv2.undistort(img, mtx, dist, None, mtx)


	# undistort
	# dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
	
	cv2.imshow("undist", undist)
	cv2.waitKey()
	# crop the image
	# x,y,w,h = roi
	# dst = dst[y:y+h, x:x+w]
	# cv2.imwrite('calibresult.png',dst)
	
	# tot_error = 0
	# mean_error = 0
	# for i in range(len(objpoints)):
	# 	imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
	# 	error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
	# 	tot_error += error

	# print ("total error: ", mean_error/len(objpoints))

if __name__ == "__main__":
	
	# Take_Pic()
	calib()
	cv2.destroyAllWindows()