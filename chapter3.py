import cv2
import numpy as np

img=cv2.imread("Resources/lambo.png")

print(img.shape)

imgResize=cv2.resize(img,(300,300))
print(imgResize.shape)

imgCropped=img[0:200,200:500]
cv2.imshow("image",img)
cv2.imshow('Image REsize',imgResize)
cv2.imshow('ImageCropped',imgCropped)

cv2.waitKey(0)

