import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
cap = cv2.VideoCapture('10.mp4')
fps = 30
while True:
    ret, frame = cap.read()
    cv2.imshow("org", frame)
    frame = cv2.resize(frame, (480, 270))
    lab = cv2.cvtColor(frame, cv2.COLOR_RGB2LAB)
    lab_planes = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab = cv2.merge(lab_planes)
    bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    bgr = cv2.cvtColor(bgr,cv2.COLOR_RGB2GRAY)
    scale = 1
    delta = 0
    ddepth = cv2.CV_64F
    blur = cv2.GaussianBlur(bgr,(5,5),10)
    blur = cv2.erode(blur,(5,5))
    grad_x = cv2.Sobel(blur, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    grad_y = cv2.Sobel(blur, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    th3 = cv2.cvtColor(grad, cv2.COLOR_GRAY2BGR)
    th3 = cv2.fastNlMeansDenoisingColored(th3,None,10,10,7,21)
    th3 = cv2.cvtColor(th3,cv2.COLOR_BGR2GRAY)
    th3 = cv2.adaptiveThreshold(th3,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,4)
    
    cv2.imshow('frame',th3)
    # time.sleep(1/fps)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
