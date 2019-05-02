import pytesseract 
from gtts import gTTS
from PIL import Image
import numpy as np
from Shakkala import Shakkala
import os
from math import ceil

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

if __name__ == "__main__":

    print("Creating text from Image")
    img = Image.open('testar.png')
    arr = np.array(img)
    textOfImage=pytesseract.image_to_string(arr,lang="ara")
    textOfImage=textOfImage.replace('»','')
    textOfImage=textOfImage.replace("'",'')
    textOfImage=textOfImage.replace('"','')
    textOfImage=textOfImage.replace(',','')

    input_text = textOfImage
    batches=ceil(len(textOfImage) / 200)
    print("Text Created successfully :",str(batches))
    folder_location = './'
    # create Shakkala object
    sh = Shakkala(folder_location, version=3)
    model, graph = sh.get_model()
    # prepare input
    finalText=""
    for i in range(batches):
        min=i*200
        if(i != (batches-1)):
            max=(i+1)*200
        else:
            max=len(textOfImage)-1
        print('the min is : ',str(min),' the max is :',str(max))
        input_text=textOfImage[min:max]
        input_int = sh.prepare_input(input_text)
        with graph.as_default():
                logits = model.predict(input_int)[0]
                predicted_harakat = sh.logits_to_text(logits)
                final_output = sh.get_final_text(input_text, predicted_harakat)
                finalText=finalText+" "+final_output


    file=open('finalArabWVText.txt','w',encoding='utf_8')
    file.write(finalText)
    tts=gTTS(textOfImage,lang='ar')
    tts.save('imgTextAr.mp3')

    print("Saved Audio")