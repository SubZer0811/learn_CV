import cv2
import numpy as np

img = cv2.imread("/home/sub0811/Desktop/practice/opencv/underwater_gate.jpeg")
cv2.imshow("orig", img)

blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("blur", blur)

blur_float = blur.astype(np.float32) / 255.0
edgeDetector = cv2.ximgproc.createStructuredEdgeDetection("model.yml")
edges = edgeDetector.detectEdges(blur_float) * 255.0

cv2.imshow("edges", edges)
cv2.waitKey()