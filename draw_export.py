import cv2
import sys

if len(sys.argv) <= 1:
    exit("Please insert the name of the image e.g. draft.jpg")    
file_name = sys.argv[1]

src = cv2.imread(file_name, 1)
tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,127,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

b, g, r = cv2.split(src)
rgba = [b,g,r, alpha]
dst = cv2.merge(rgba,4)


fromCenter = True
cv2.namedWindow("Select ROIs",2)
ROIs = cv2.selectROIs("Select ROIs", dst, fromCenter)


import os
if not os.path.exists("draft_parts/"):
    os.makedirs("draft_parts/")

    
n_cnt = 0
for parts in ROIs:
    ROI_1 = dst[parts[1]:parts[1]+parts[3], parts[0]:parts[0]+parts[2]]
    cv2.imwrite("draft_parts/part_"+str(n_cnt)+".png", ROI_1)
    #cv2.imshow("part_"+str(n_cnt),ROI_1)
    n_cnt +=1
    
cv2.waitKey(0)
cv2.destroyAllWindows()


