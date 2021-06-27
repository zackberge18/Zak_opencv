#####Chapter 1
### for IMages
# import cv2
#
# img=cv2.imread("Resources/lena.jpeg")
#
# cv2.imshow("output",img)
# cv2.waitKey(5000)


#for Videos
# import cv2
# 
# cap=cv2.VideoCapture("Resources/test_video.mp4")
# while True:
#     success, img=cap.read()
#     cv2.imshow("video", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break


##for WEbcam
import cv2

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,50)
while True:
    success, img=cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
