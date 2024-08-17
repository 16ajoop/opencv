#spliting the webcam into 4parts 
import numpy as np
import cv2

# load a video captured ( capture as cap )
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()                 #ret tells that whether the cap is working or not
    
    # to get the wedth and height of the img width = 3, height = 4
    width = int(cap.get(3))
    height = int(cap.get(4))

    # making it 4set of img
    # create a blank image        #unsigned int 8-bit
    image = np.zeros(frame.shape, np.uint8)

    # resizing the frame(shirnking both width and height by half)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    #taking the small frame & pasting it in  the blank-img
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)     #pasting in top-left #syntax to rotate_180
    image[height//2:, :width//2] = smaller_frame     #bottom-left
    image[:height//2, width//2:] =  cv2.rotate(smaller_frame, cv2.ROTATE_180)      #top-right
    image[height//2:, width//2:] = smaller_frame     #bottom-right


    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()                               #freeup the webcam
cv2.destroyAllWindows()
