import cv2 as cv

img = cv.imread(r'D:\Python_Folder\opencvPractice\blue.jpg')
print(img)
print(img[1, 1, 0])  # print(img[1][1][0])  same as indexing

cv.imshow('bubbly', img)
# cv.waitKey(0)


# width = int(img.shape[1] * 0.3)
# length = int(img.shape[0] * 0.3)
# new_img = cv.resize(img, (width, length), interpolation=cv.INTER_AREA)
# cv.imshow('photooooooooooooo', new_img)
# cv.waitKey(0)
