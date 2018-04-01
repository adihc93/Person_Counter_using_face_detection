# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:51:15 2018

@author: HP
"""

import cv2

#import sys



faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
 


video_capture = cv2.VideoCapture(0)



while True:
 
    count=0
    ret, frame = video_capture.read()
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    faces = faceCascade.detectMultiScale(gray, 1.1, 10)
 
    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count+=1
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,50)
    fontScale              = 1
    fontColor              = (0,0,255)
    lineType               = 2
    strng='No of persons:'+str(count)

    cv2.putText(frame,strng, 
                bottomLeftCornerOfText, 
                font, 
                fontScale,
                fontColor,
                lineType)        
 
    cv2.imshow('Video', frame)



    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
   
video_capture.release()

cv2.destroyAllWindows()