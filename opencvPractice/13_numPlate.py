import cv2 as cv
import numpy as np
import pytesseract
img_car_org = cv.imread(
    r'D:\Python_Folder\opencvPractice\ind_car.jpeg')


# the function detects and perfors blurring on the number plate.
def extract_plate(img):
    plate_img = img.copy()

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

    return plate_img, plate  # returning the processed image.


one, two = extract_plate(img_car_org)
cv.imshow('one', one)
cv.imshow('two', two)



cv.imwrite(r'D:\Python_Folder\opencvPractice\car_google2_cropDilated.jpeg', two)
# text recognition
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\vivek\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

_, two = cv.threshold(two, 50, 255, cv.THRESH_BINARY_INV)
cv.imshow('twob', two)


cv.waitKey(0)

cv.destroyAllWindows()
text = pytesseract.image_to_string(two)
print(text)
