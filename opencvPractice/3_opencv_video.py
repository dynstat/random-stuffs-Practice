import cv2 as cv

cap = cv.VideoCapture(r'D:\Python_Folder\opencvPractice\seno.mp4')


if __name__ == '__main__':
    while True:
        i, frame = cap.read()
        if i == True:
            cv.imshow('seno video', frame)
        if cv.waitKey(40) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
