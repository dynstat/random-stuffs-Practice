import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

codec = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter(
    r'D:\Python_Folder\opencvPractice\test.avi', codec, 25.0, (640, 480))  # 4:3

while cap.isOpened():
    isTrue, frame = cap.read()
    if isTrue:
        cv.imshow('test', frame)
        # print((frame.shape))

        out.write(frame)  # to save the videoCapture as a file
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
out.release()
cv.destroyAllWindows()
