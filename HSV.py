#Dedecting color 
# converting BGR img into HSV  --->hue saturation and lightness/brightness
import numpy as np
import cv2
 
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
       
       # converting normal img into hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

       # define lowerboud & upperbound for the pixels
    lower_blue = np.array([90, 50, 50])    #lighter_blue
    upper_blue = np.array([130, 255, 255])  #darker_blue

    # masks- a part of image
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # comapre each pixels with the mask and returns only them
    result = cv2.bitwise_and(frame, frame, mask=mask)          # &-operator here!!

    cv2.imshow('frame', result)
    # cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

















