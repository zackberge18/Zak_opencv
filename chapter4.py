import cv2
import numpy as np


def Draw_me():
    a,b,c,d=0,0,0,0
    while True:
        if a<b:
            break
        a = np.random.randint(512)
        b = np.random.randint(512)
    while True:
        if c<d:
            break
        c = np.random.randint(512)
        d = np.random.randint(512)

    e = np.random.randint(256)
    f = np.random.randint(256)
    g = np.random.randint(256)

    return a, b, c, d,e,f,g


img=np.zeros((512,512,3),np.uint8)
for i in range(50):
    a, b, c, d, e, f,g = Draw_me()
    # print(a, b, c, d,g )
    # img[a:b, c:d] = g, e, f
    #cv2.rectangle(img,(c,d),(a,b),(e,f,g),2)
    #a, b, c, d, e, f, g = Draw_me()
    
    #cv2.line(img,(a,b),(c,d),(e,f,g),3)
    #a, b, c, d, e, f, g = Draw_me()
    #cv2.circle(img,(a,b),int(d/4),(e,f,g),5)
    cv2.putText(img,"Azra Zelal",(a,b),cv2.FONT_HERSHEY_TRIPLEX,2,(e,f,g),1)
cv2.imshow("image",img)

cv2.waitKey(0)


