import pytesseract 
from gtts import gTTS
from PIL import Image
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('test.jpg')
arr = np.array(img)
textOfImage=pytesseract.image_to_string(arr,lang="ara")
textOfImage=''' لِكُلِّ إنْسَانٍ حَقٌّ أَلْتَمَتُّعُ بِكَافَّةٍ لِقُوقٍ وَأَلْحَرِيَّاتٍ أَلْوَارِدَةٍ فِي هَذَا
الْإِعْلَانِ دُونَ أَيْ تَمْيِيزُ كَالتَّمْيِيزِ بِسَبَبِ أَلْعَنْصِرٍ أَوْ أَلْلُوْنَ أَوْ
أَجْنَسَ أَوْ ا لِلُغَةً أَوْ آلِدَيْنِ أَوَآلِرَأْي ا لِسَيَاسِي أَوأَي رَأَ يَآخَرِءُ أَوْ
الْأَاصِلُ أَ لِوَطْنِيٍّ أَوْ أَلِاجْتِمَاعِيٌّ أَوْ  أَلْثَرُوَةَ أَوَالْمِيلَادِ أَوأَي وَضْعُ
آخَرَءُ دُونَ أَيَّةِ ثَفْرَقَةٍ بَيْنَ أَ لِرِجَالٍ وَآلنِسَاءِ. وَفَضْلًا عَمَّا تَقَدَّمَ فَلَنَ
يَحْكُونَ هُنَّكَ أَيْ فَيْزَ أَسَاسَهُ أَلْوَضَعَ السَّيَاسِيّ أ وَأَلْقَانُونٍَ أَوْ
أَلْدُولِي لِبَادٍ أَوْ آلْبَقْعَةُ أَلْتِي يَنْتَمِي إلَيْهَا أَ لِنَرْدٍ سَوَاءٌ كَانَ هَذَا آلِبًا د أَوْ
نِلَكَ أَلْبَقْعَةَ مُسْتَقِلًّا أَوْ تَحْتَ آلُوصَايَةٍ أَوْ غَيْرِ مُتَمَتِّعٍ بِالْحَكْرِ
أَلْذَاتِيِّ أَوْكَانَتْ سَيَادِئِهِ خَاضِعَةً لِأَيِّ قَيْدٍ مِنْ أَلْقُيُودَ'''
tts=gTTS(textOfImage,lang='ar')
tts.save('imgTextArSh.mp3')