# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:42:15 2018

@author: HP
"""

import cv2
import tkinter 
from tkinter.filedialog import askopenfilename
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
print("Enter file path: ")
tkinter.Tk().withdraw()
filename = askopenfilename()
count=0
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    count+=1

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,50)
fontScale              = 1
fontColor              = (0,0,255)
lineType               = 2
strng='No of persons:'+str(count)

cv2.putText(img,strng, 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    lineType)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()