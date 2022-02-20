import cv2 as cv
# import opencv_video as vid

img = cv.imread(r'D:\Python_Folder\opencvPractice\halo.jpg', 0)
# cap = cv.VideoCapture(r'D:\Python_Folder\opencvPractice\seno.mp4')
# cv.imshow('halofromimshow', img)

# resizing
# with open('img_matrix.txt', 'w') as f:
#     f.write(str(img))


# def resizer(src, factor):
#     width = int(src.shape[1] * factor)
#     length = int(src.shape[0] * factor)
#     dimen = (width, length)
#     return cv.resize(src, dimen, interpolation=cv.INTER_AREA)


# new_img = resizer(img, 0.3)
cv.imshow('Bubbly', img)
cv.waitKey(0)  # 0 --> wait forever

# while True:
#     isTrue, vidframe = cap.read()
#     if isTrue == True:
#         vidframe = resizer(vidframe, 0.5)
#         cv.imshow("senoWaliVideo", vidframe)
#         if cv.waitKey(30) & 0xFF == ord('q'):   # 11010011 & 11111111
#             break
