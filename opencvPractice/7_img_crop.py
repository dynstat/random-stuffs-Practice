import cv2 as cv
import numpy as np


img = cv.imread(r'D:\Python_Folder\opencvPractice\scenery.jpg')

# img = cv.resize(img, (1120, 630))

#(1285,2160)  (2200,2160)  (1285,1000) (2200,1000)
# x1,y1,x2,y2
# x1 = 1285, x2 = 2200, y1 = 2160, y2 = 1000

cropped_img = img[1000:2160, 1285:2200]
cropped_img = cv.resize(cropped_img, (375, 665))
# cropped_img = cv.cvtColor(cropped_img, cv.COLOR_RGB2BGR)
# print(img[1000:2160, 1285:2200])
cv.imshow('resized', cropped_img)
cv.waitKey(0)
