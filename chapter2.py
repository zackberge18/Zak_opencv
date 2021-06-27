import cv2
import numpy as np


img=cv2.imread("Resources/lena.png")
#define kernel with numpy
kernel=np.ones((3,3),np.uint8)
#Turn to grayScale
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray to blur
imgBlur=cv2.GaussianBlur(imgGray,(5,5),0)
## img to Canny
imgCanny=cv2.Canny(img,100,100)
## Canny to dialation
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("GrayScale",imgGray)
cv2.imshow("BlurScale",imgBlur)
cv2.imshow("CannyScale",imgCanny)
cv2.imshow("DialationScale",imgDialation)
cv2.imshow("ErodedScale",imgEroded)
cv2.waitKey(0)