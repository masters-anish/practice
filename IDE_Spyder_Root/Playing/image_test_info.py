
import cv2

grey_img = cv2.imread("./images/test_image_hyper.png", 0)
color_img = cv2.imread("./images/test_image_hyper.png", 1)

#images opened using cv2 are numpy arrays
print(type(grey_img)) 
print(type(color_img)) 

# Use the function cv2.imshow() to display an image in a window. 
# First argument is the window name which is a string. second argument is our image. 

cv2.imshow("pic", grey_img)
cv2.imshow("color pic", color_img)

# Maintain output window until 
# user presses a key or 1000 ms (1s)
cv2.waitKey(0)          

#destroys all windows created
cv2.destroyAllWindows() 

#OpenCV imread, imwrite and imshow all work with the BGR order, not RGB
#but there is no need to change the order when you read an image with 
#cv2.imread and then want to show it with cv2.imshow
#if you use matplotlib, it uses RGB. 

import matplotlib.pyplot as plt
plt.imshow(color_img)  

#OpenCV represents RGB images as multi-dimensional NumPy arrays, but as BGR.

#we can convert the images from BGR to RGB
plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB))

#We can also change color spaces from RGB to HSV..
plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV))