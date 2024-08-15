# to copy a part of img and paste it some where else

import cv2

img = cv2.imread(r'C:\Users\\POOJA\\Downloads\\quote.jpeg',-1)

# to chose which part to copy from
copy = img[500:700, 600:900]

# and paste to
img[100:300, 650:950] = copy

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()