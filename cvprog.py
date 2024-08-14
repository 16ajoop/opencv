# python opencv prog to display & modify the img
import cv2

# load the image
img = cv2.imread(r"C:\Users\POOJA\OneDrive\Pictures\flowers.jpg",1)

# resizing by pixles
img = cv2.resize(img,(400,400))                   
# if u want to reduce the image size by half then : img = cv2.resize(img, (0,0) , fx=0.5

# to rotate 
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)            #to save the updated img : cv2.imwrite('new_img.jpg',img)

# to display
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
