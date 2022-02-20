import pafy
import cv2 as cv

url = 'https://youtu.be/jEJI6Nf1aWU'
myvid = pafy.new(url)
print(myvid)

myvid = myvid.getbest(preftype='mp4')

cap = cv.VideoCapture(myvid.url)

while True:
    isTrue, frame = cap.read()
    if isTrue:
        cv.imshow('yt', frame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
