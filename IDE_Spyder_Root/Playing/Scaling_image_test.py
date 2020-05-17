#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:56:46 2020

@author: anish
"""


import cv2

img = cv2.imread("./images/test.jpeg", 1)   #Color is BGR not RGB

#use cv2.resize. Can specify size or scaling factor.
#Inter_cubic or Inter_linear for zooming.
#Use INTER_AREA for shrinking
#Following xample zooms by 2 times.

resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow("original pic", img)
cv2.imshow("resized pic", resized)
cv2.waitKey(0)          
cv2.destroyAllWindows() 