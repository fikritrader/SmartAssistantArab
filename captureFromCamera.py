# -*- coding: utf-8 -*-
import numpy as np
import cv2
from PIL import Image
import pytesseract
from gtts import gTTS
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (100,100)
fontScale              = 1
fontColor              = (255,0,0)
lineType               = 2

waitTime=5
minChars=200

oldTime=time.time()
willPredict=False
resultText=""
def cleanText(text):
    finaltext=""
    for char in text:
        if char.isalpha() or char == " " or char == "\n":
            finaltext=finaltext+char
    return finaltext

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    if (time.time() >= oldTime+waitTime and willPredict==False):
        oldTime=time.time() 
        willPredict=True
    if willPredict:
        result = pytesseract.image_to_string(gray,lang="ara")
        gray = cv2.putText(gray,result, bottomLeftCornerOfText,font,fontScale,fontColor,lineType)

        charLen=len(result)
        if charLen==0:
            print("looking for text to read ..")
        else:
            print("the lenght of the predicted text is :",charLen,"it needs to be at least 200")
        if(len(result) >= minChars):
            file=open("textAra.txt",'w',encoding='utf_8')
            result =cleanText(result)
            file.write(result)
            willPredict=False
            oldTime=time.time()+waitTime
            resultText=result
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        willPredict=False
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
tts=gTTS(resultText,lang='ar')
tts.save('finalAudio.mp3')