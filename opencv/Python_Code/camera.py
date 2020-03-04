import cv2
import numpy as np
import matplotlib.pyplot as plt 
#%matplotlib inline 

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_stress_test.avi', fourcc, 20.0, (640, 480))


while(1):
	if cap.isOpened():
		print ("We are in")
		ret, frame = cap.read()
		plt.show(frame)
		out.write(frame)
	else: 
		print ("sorry bro")

cap.release()
out.release()
cv2.destroyAllWindows()
