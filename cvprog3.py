# drawing lines
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
                  #src img #starting posi #ending posi #color #thickness
    img = cv2.line(frame, (0,0), (width,height), (255,0,0), 10)
    img = cv2.line(frame, (0,height), (width,0), (0,255,0), 10)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()                               #freeup the webcam
cv2.destroyAllWindows()