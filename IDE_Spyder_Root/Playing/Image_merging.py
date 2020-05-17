#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:07:32 2020

@author: anish
"""


import cv2

grey_img = cv2.imread("./images/test.jpeg", 0) 
img = cv2.imread("./images/test.jpeg", 1)   #Color is BGR not RGB

print(img.shape)     #(586, 415, 3)
print("Top left", img[0,0])    #Top left pixel
print("Top right", img[0, 200])  # Top right
print("Bottom Left", img[165, 0]) # Bottom left
print("Bottom right", img[165, 250])  # Bottom right

#cv2.imshow("color pic", img)
#cv2.waitKey(0)          
#cv2.destroyAllWindows() 

#Split and merging channels
#Show individual color channels in the image
blue = img[:, :, 0]   #Show only blue pic. (BGR so B=0)
green = img[:, :, 1]  #Show only green pixels
red = img[:, :, 2]  #red only

"""
cv2.imshow("red pic", red)
cv2.waitKey(0)          
cv2.destroyAllWindows() 
"""

#Or split all channels at once

b,g,r = cv2.split(img)

cv2.imshow("green pic", g)
cv2.waitKey(0)          
cv2.destroyAllWindows() 

#to merge each image into bgr

img_merged = cv2.merge((b,g,r))

cv2.imshow("merged pic", img_merged)
cv2.waitKey(0)          
cv2.destroyAllWindows() 