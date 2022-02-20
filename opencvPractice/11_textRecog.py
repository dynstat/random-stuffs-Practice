import pytesseract
import cv2
# from PIL import Image

path = r'C:\Program Files (x86)\Tesseract-OCR\tessaract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\vivek\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
img = cv2.imread(r'D:\Python_Folder\opencvPractice\notif.png')
# # img = Image.open('notif.png')
text = pytesseract.image_to_string(img)
print(text)
