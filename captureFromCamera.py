# -*- coding: utf-8 -*-
import numpy as np
import cv2
from PIL import Image
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (100,100)
fontScale              = 1
fontColor              = (255,0,0)
lineType               = 2

waitTime=5
oldTime=time.time()
willPredict=False
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if (time.time() >= oldTime+waitTime and willPredict==False):
        oldTime=time.time() 
        willPredict=True
    if willPredict:
        result = pytesseract.image_to_string(gray,lang="ara")
        gray = cv2.putText(gray,result, bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
        print("the lenght of the predicted text is :",len(result))
        if(len(result) >= 100):
            file=open("textAra",'w',encoding='utf_8')
            file.write(result)
            willPredict=False
            oldTime=time.time()+waitTime
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()