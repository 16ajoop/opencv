# drawing lines & text
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0), (width,height), (255,0,0), 10)
    font = cv2.FONT_HERSHEY_SIMPLEX                             #bottom_left_hand_corner ,scale=magnifier(2) ,color(0,0,0)-->black, thickness=3
    img = cv2.putText(img, 'comes great responsibility!', (200, height -10), font, 1 ,(0, 0, 0), 3, cv2.LINE_AA)



    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()                               #freeup the webcam
cv2.destroyAllWindows()