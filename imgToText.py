# -*- coding: utf-8 -*-
import pytesseract
from gtts import gTTS
from PIL import Image
import numpy as np
import cv2
#from Shakkala import Shakkala
import os
from math import ceil

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_string(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    # Remove template file
    #os.remove(temp)

    return result


if __name__ == "__main__":

    print("Creating text from Image")
    img = Image.open('myimg.jpg')
    arr = np.array(img)
    textOfImage=pytesseract.image_to_string(arr,lang="eng")
    textOfImage=textOfImage.replace('»','')
    textOfImage=textOfImage.replace("'",'')
    textOfImage=textOfImage.replace('"','')
    textOfImage=textOfImage.replace(',','')
    input_text = textOfImage
    batches=ceil(len(textOfImage) / 200)
    print("Text Created successfully :",str(batches))
    folder_location = './'

    file=open('finalArabWVText.txt','w',encoding='utf_8')
    file.write(textOfImage)
    #tts=gTTS(textOfImage,lang='ar')
    #tts.save('imgTextAr.mp3')

    print("Saved Audio")