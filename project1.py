import cv2
import numpy as np
cap=cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,50)

myColors=[[0,43,56,213,68,255],[133,56,0,159,156,255],
          [57,76,0,100,255,255]]
myColorValues=[[51,153,255],
               [255,0,255],
               [0,255,0]]
def findColor(img,myColors):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(myColors[0][0:3])
    upper = np.array(myColors[0][3:6])

    mask = cv2.inRange(imgHsv, lower, upper)
    x,y=getContours(mask)
    cv2.circle(imgResult,(x,y),10,(255,25,0),cv2.FILLED)
    #cv2.imshow("img",mask)

def drawONCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),(255,25,128),cv2.FILLED)
def getContours(img):

    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)

        if area>500:
            cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgResult,(x,y),(x+w,y+h),(0,255,0),3)
    return x+w//2,y
while True:
    success, img=cap.read()
    imgResult=img.copy()
    findColor(img,myColors)
    cv2.imshow("video", imgResult)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
