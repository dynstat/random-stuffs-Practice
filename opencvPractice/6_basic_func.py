import cv2 as cv
import numpy as np

img = cv.imread(r'D:\Python_Folder\opencvPractice\car_google2.jpeg')
img_gray = cv.imread(r'D:\Python_Folder\opencvPractice\car_google2.jpeg', 0)
# img_gray = cv.resize(img_gray, (640, 480))
cv.imwrite(r'D:\Python_Folder\opencvPractice\car_google2_edit.jpeg', img_gray)

img_gray_blur = cv.GaussianBlur(img_gray, (11, 11), cv.BORDER_CONSTANT)
# cv.imshow('blur', img_gray_blur)
cv.imwrite(
    r'D:\Python_Folder\opencvPractice\car_google2_edit_blur.jpeg', img_gray_blur)


edge_img = cv.Canny(img_gray_blur, 10, 90)
# cv.imshow('edge', edge_img)
cv.imwrite(r'D:\Python_Folder\opencvPractice\car_google2_edit_canny.jpeg', edge_img)


# morphological Transformation
kernel = np.ones((3, 3), np.uint8)  # 5x5 kernel with full of ones.
cv.imshow('k', kernel)
cv.waitKey(0)
# e = cv.erode(edge_img, kernel)
d = cv.dilate(edge_img, kernel)
cv.imshow('erosion', d)
cv.imwrite(r"D:\Python_Folder\opencvPractice\car_google2_dilated.jpeg", d)


# h, w, ch = img.shape  # [w,h,ch]  ,   img.shape[2]
# h2, w2 = img_gray.shape  # [w,h]  ,   grayscale image
# new_img = cv.adaptiveThreshold(
#     img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

# cv.imshow('ADV', new_img)

# print(img)
# print(f'w = {w}\nh = {h}\nchannels = {ch}\n\n\n')
# cv.imshow('normal', img)
# cv.waitKey(0)

# print(img_gray)
# print(f'w = {w2}\nh = {h2}\n')
# cv.imshow('gray', img_gray)

# cv.imshow('ye lo', img)
# cv.waitKey(0)


# def resizer(src, factor):
#     width = int(src.shape[1] * factor)
#     length = int(src.shape[0] * factor)
#     dimen = (width, length)
#     return cv.resize(src, dimen, interpolation=cv.INTER_AREA)


# img = resizer(img, 0.3)
# chhoti_img = cv.imwrite('chhoti_scenery.jpg', img)
# bw_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # BGR to GRAY
# # cv.imshow('ye lo', bw_img)

# # blur_img = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# blur_img = cv.medianBlur(img, 3)
# # cv.imshow('blur', blur_img)

# edge_img = cv.Canny(blur_img, 10, 90)
# # cv.imshow('edge', edge_img)
# # cv.waitKey(0)


# # c(558,357), left(312, l), right(764,l)
# def region_of_int(src_img):
#     # sourcery skip: inline-immediately-returned-variable
#     l = img.shape[0]
#     region = np.array([(558, 357), (312, l), (764, l)])
#     mask = np.zeros_like(img)
#     cv.fillPoly(mask, region, 255)
#     masked_img = cv.bitwise_and(edge_img, mask)
#     return masked_img


# cv.imshow('mask', region_of_int(img))

cv.waitKey(0)
