import cv2 as cv
import numpy as np
# from matplotlib import pyplot as plt

img_car_org = cv.imread(r'D:\Python_Folder\opencvPractice\car_img.jpg')
img_car_gray = cv.cvtColor(img_car_org, cv.COLOR_RGB2GRAY)

cv.imshow('gray', img_car_gray)

plate_img = img_car_org.copy()

# Loads the data required for detecting the license plates from cascade classifier.
plate_cascade = cv.CascadeClassifier(
    r'D:\pythoninstall39\Lib\site-packages\cv2\data\haarcascade_russian_plate_number.xml')

# detects numberplates and returns the coordinates and dimensions of detected license plate's contours.
plate_rect = plate_cascade.detectMultiScale(
    plate_img, scaleFactor=1.3, minNeighbors=7)

for (x, y, w, h) in plate_rect:
    # parameter tuning
    # a, b = (int(0.02*img.shape[0]), int(0.025*img.shape[1]))
    plate = plate_img[y:y+h, x:x+w, :]
    # finally representing the detected contours by drawing rectangles around the edges.
    cv.rectangle(plate_img, (x, y), (x+w, y+h), (51, 51, 255), 3)
cv.imshow('one', plate_img)
# edge detection
b_filter = cv.bilateralFilter(img_car_gray, 15, 17, 17)
blur = cv.GaussianBlur(img_car_gray, (7, 7), cv.BORDER_DEFAULT)
edge = cv.Canny(blur, 50, 200)


cv.imshow('edge', edge)

contours, h = cv.findContours(
    edge, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key=cv.contourArea, reverse=True)[:10]
# print(type(contours))
loc = None
for cont in contours:
    approx = cv.approxPolyDP(cont, 10, True)
    if len(approx) == 4:
        loc = approx
        print("approx", loc)

    # black background of same size as the original image
    background = np.zeros(img_car_gray.shape, np.uint8)

    cv.drawContours(background, [approx], 0, 255, -1)
    newImage = cv.bitwise_and(img_car_org, img_car_org, mask=background)

    # cv.imshow("final", newImage)
    cv.imshow("background", background)

    cv.waitKey(0)
cv.destroyAllWindows()
