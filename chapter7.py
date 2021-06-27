import cv2
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver



path="Resources/lambo.png"
def empty(a):
    pass
cv2.namedWindow("trackBars")
cv2.resizeWindow("trackBars",640,300)
cv2.createTrackbar("Hue Min","trackBars",0,179,empty)
cv2.createTrackbar("Hue Max","trackBars",179,179,empty)
cv2.createTrackbar("Sat Min","trackBars",0,255,empty)
cv2.createTrackbar("Sat Max","trackBars",255,255,empty)
cv2.createTrackbar("Val Min","trackBars",0,255,empty)
cv2.createTrackbar("Val Max","trackBars",255,255,empty)
while True:
    img = cv2.imread(path)
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min",'trackBars')
    h_max=cv2.getTrackbarPos("Hue Max",'trackBars')
    s_min=cv2.getTrackbarPos("Sat Min",'trackBars')
    s_max=cv2.getTrackbarPos("Sat Max",'trackBars')
    v_min=cv2.getTrackbarPos("Val Min",'trackBars')
    v_max=cv2.getTrackbarPos("Val Max",'trackBars')
    print(h_min,h_max,s_max,s_min,v_max,v_min)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHsv,lower,upper)
    imgResult=cv2.bitwise_and(img,img,mask=mask)
   
    
    imgStack= stackImages(0.6,([img,imgHsv],[mask,imgResult]))
    cv2.imshow("stacked images",imgStack)
    cv2.waitKey(100)
