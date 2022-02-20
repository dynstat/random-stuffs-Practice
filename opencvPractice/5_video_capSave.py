import cv2 as cv
import numpy as np

cap = cv. VideoCapture(0)
cap.open(r'D:\Python_Folder\opencvPractice\seno.mp4')
cap.set(cv.CAP_PROP_POS_MSEC)
# cv.setMouseCallback('something', draw, param=int)
while cap.isOpened():
    isTrue, frame = cap.read()
    if isTrue == True:
        cv.imshow('somethig', frame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
cap.release()
cv.destroyAllWindows()
