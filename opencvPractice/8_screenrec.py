import cv2 as cv
import numpy as np
import pyautogui as pgui


codec = cv.VideoWriter_fourcc(*'XVID')  # 'X','V','I','D'
out = cv.VideoWriter(
    r'D:\Python_Folder\opencvPractice\screeRec.avi', codec, 25.0, (1366, 768))


while True:
    img = pgui.screenshot()
    img = np.array(img)
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

    # writing the each frame receiving from the read() function, to the locations and parameters set by the VideoWriter funcrtion
    out.write(img)

    if cv.waitKey(1) == ord('q'):
        break

out.release()
cv.destroyWindow()
