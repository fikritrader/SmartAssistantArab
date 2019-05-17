# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
import numpy as np
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  

img = cv2.imread("img.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
#img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

# Write the image after apply opencv to do some ...
cv2.imwrite("thres.png", img)

# Recognize text with tesseract for python
img=Image.open("thres.png")
arr = np.array(img)
result = pytesseract.image_to_string(arr,lang="ara")
# Remove template file
#os.remove(temp)
file=open('finalArabWVText.txt','w',encoding='utf_8')
file.write(result)
print("the result is : "+result)