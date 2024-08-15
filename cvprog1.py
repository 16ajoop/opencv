import cv2
import random
img = cv2.imread(r'C:\Users\\POOJA\\Downloads\\quote.jpeg',-1)

# looping though 1st 100rows
for i in range(100):
    for j in range(img.shape[1]):
                    #[row, column, channels]---->with_lowerbound_0 & upperbound_255            
        img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# to print the numpy values of img the o/p :(648,648,3) 
# here in() pos1_rep_height(row), pos2_rep_width(column), pos3_rep_channels(how many colors rep the img)
# -->print(img.shape)

# standard is RGB- red, green, blue but in opencv uses BGR- blue, green, red 
# blue green red
# [255, 0   ,  0] ---------> blue, no_green, no_red

# to print the first row of img by specifiying index_pos
# -->print(img[0])


# to see one pixles perticularly
# -->print(img[257][400])/

