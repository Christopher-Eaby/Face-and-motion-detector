# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`        C.E.
         
Created on Thu Aug 20 16:22:19 2020
@author: Chris
Contact :
    Christopher.eaby@gmail.com
"""

import numpy as np
import cv2

Threshhold = 10
font = cv2.FONT_HERSHEY_SIMPLEX
#TODO: Face Detection 1
amount = 0

def distMap(f1, f2):
    """outputs pythagorean distance between two frames"""
    f1_32 = np.float32(f1)
    f2_32 = np.float32(f2)
    diff32 = f1_32 - f2_32
    norm32 = np.sqrt(diff32[:,:,0]**2 + diff32[:,:,1]**2 + diff32[:,:,2]**2)/np.sqrt(255**2 + 255**2 + 255**2)
    dist = np.uint8(norm32*255)
    return dist

cv2.namedWindow('Normal')
cv2.namedWindow('Motion')

cap = cv2.VideoCapture(0)

_, f1 = cap.read()
_, f2 = cap.read()

facecount = 0
while(True):
    _, f3 = cap.read()
    rows, cols, _ = np.shape(f3)
    cv2.imshow('Motion', f3)
    dist = distMap(f1, f3)

    f1 = f2
    f2 = f3

    mod = cv2.GaussianBlur(dist, (9,9), 0)

    _, thresh = cv2.threshold(mod, 100, 255, 0)

    _, Dev = cv2.meanStdDev(mod)

    cv2.imshow('Motion', mod)
    if Dev > Threshhold:
        amount += 1
    cv2.imshow('Normal', f2)
    
    if cv2.waitKey(1) & 0xFF == 27:
        print("Times movement was noticed : " + str(amount))
        break
    

cap.release()
cv2.destroyAllWindows()
