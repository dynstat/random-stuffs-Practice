import cv2 as cv
import numpy as np

img_p = cv.imread(r'D:\Python_Folder\opencvPractice\pebbles.jpg')
img_bird_org = cv.imread(r'D:\Python_Folder\opencvPractice\Bird.jpg')

img_bird_org = cv.resize(img_bird_org, (600, 330))
img_bird_gray = cv.cvtColor(img_bird_org, cv.COLOR_BGR2GRAY)

blank = np.zeros((600, 330, 3), np.uint8)
cv.imshow('bird resized', img_bird_gray)

# k = cv.adaptiveThreshold(
# img_bird_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 3, 4)
r, k = cv.threshold(img_bird_gray, 100, 255, cv.THRESH_BINARY)
# img_blur = cv.GaussianBlur(img_bird, (7, 7), cv.BORDER_DEFAULT)
# img_edge = cv.Canny(img_blur, 10, 60)
# cv.imshow('edge', img_edge)
# cv.imshow('mask', k)

c, h = cv.findContours(k, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.drawContours(blank, c, -1, (124, 255, 21), -1)

print(f"c = {c},h = {h}")

# # mix_bird = cv.bitwise_and(img_bird_org, img_bird_org, mask=k)
cv.imshow('mix', k)
cv.imshow('c', blank)

cv.waitKey(0)
cv.destroyAllWindows()
