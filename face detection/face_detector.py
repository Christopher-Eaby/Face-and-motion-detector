# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`        C.E.
         
Created on Thu Aug 20 14:52:10 2020
@author: Chris
Contact :
    Christopher.eaby@gmail.com
"""

import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

capture = cv2.VideoCapture(0)

while True:
    _, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces: 
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 60, 0), 2)
        grayeye = gray[y:y+h, x:x+w]
        eyecolor = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(grayeye, 1.3, 4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(eyecolor, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    
    cv2.imshow('img', img)
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break
  
capture.release()
cv2.destroyAllWindows()

