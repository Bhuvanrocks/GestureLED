# Author: Bhuvan Kumar
# GitHub: Bhuvanrocks
# Description: Python Code for controlling the brightness of LED using gestures
from cvzone.SerialModule import SerialObject
import cv2
import time
import HTM
import math
import numpy as np

arduino=SerialObject('COM4')

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
pTime,cTime=0,0
pTime2,cTime2=0,0
detector=HTM.HandTracker(detectionCon=0.7)

vol,volBar,volPer=0,0,0

while True:
    success,img=cap.read()
    img=detector.handsFinder(img)
    lmList=detector.positionFinder(img,draw=False)
    #print(lmList)
    cTime2=time.time()
    if len(lmList) != 0:
        #print(lmList[4],lmList[8])
        x1,y1,x2,y2=lmList[4][1],lmList[4][2],lmList[8][1],lmList[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2
        cv2.circle(img,(x1,y1),10,(0,255,0),cv2.FILLED)

        cv2.circle(img,(x2, y2), 10, (0, 255, 0), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)
        cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)
        length=math.hypot(x2-x1,y2-y1)
        volPer=np.interp(length,[50,150],[0,100])
        cv2.putText(img,f'{int(volPer)} %',(40,450),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),2)
        arduino.sendData([volPer])
        if length<50:
            cv2.circle(img,(cx,cy),10,(0,255,255),cv2.FILLED)

    cTime=time.time()
    fps=int(1//(cTime-pTime))
    pTime=cTime
    cv2.putText(img,f'FPS{fps}',(40,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),2)
    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
