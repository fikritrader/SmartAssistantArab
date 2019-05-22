from gtts import gTTS
from PIL import Image
import numpy as np

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#img = Image.open('test.jpg')
#arr = np.array(img)
#textOfImage=pytesseract.image_to_string(arr,lang="ara")
textOfImage='''حاضر أنا احبك لأنك جميلة جدا  ولأن صوتك رائع ولأنك
تهتمين بي وتحبيني ولان روحك كلها أمل وتفاؤل ولأن
ابتسامتك ساحرة وجذابة وأحب كل حركة تقومين بها وكل
خطوة تمشينها هل هذا الكلام مقنع لك أرجو ذلك'''
tts=gTTS(textOfImage,lang='ar')
tts.save('imgTextArSh.mp3')