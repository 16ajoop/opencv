# To assess the webcam!!!!
import numpy as np
import cv2

# load a video captured ( capture as cap )
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()                 #ret tells that whether the cap is working or not

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()                               #freeup the webcam
cv2.destroyAllWindows()
