from datetime import date
import datetime
import speech_recognition as sr
import re
from gtts import gTTS
import os
from playsound import playsound
r=sr.Recognizer()
with sr.Microphone() as source:
    print("say something")
    audio=r.listen(source)
    print("time over, thanks")
try:
    # print("TEXT :"+r.recognize_google(audio,language='ar'))
    text=r.recognize_google(audio,language='ar')
    print(text)
except:
    pass  
mot1 = 'تاريخ'
mot2 = 'اليوم'
parol = text.split(" ")
if mot1 in text :
    if mot2 in text :        
        todaytime =  datetime.datetime.now()
        #print(str(todaytime))
        possible_characters = (':', ' ', '-', '.')
        date = re.split("[%s]" % ("".join(possible_characters)), str(todaytime))
        #print(date)

if date[1] == '01':
     day = '	يناير'
else: 
     if date[1] == '02':
         day = 'فبراير'
     else :
         if date[1] == '03':
             day = 'مارس'
         else:
             if date[1] == '04':
                 day = 'ابريل'
             else :
                 if date[1] == '05':
                     day = 'ماي'
                 else : 
                     if date[1] == '06':
                         day = 'يونيو'
                     else:
                         if date[1] == '07':
                             day = 'يوليوز'
                         else:
                             if date[1] == '08':
                                 day = 'غشت'
                             else:
                                 if date[1] == '09':
                                     day = 'شتنبر'
                                 else:
                                     if date[1] == '10':
                                         day = 'اكتوبر'
                                     else:
                                         if date[1] == '11':
                                             day = 'نونبر'
                                         else:
                                           if date[1] == '12':
                                               day = 'دجنبر'


text = "اليوم هو"+date[2]+ " من "+day+ " لعام  "+date[0]+ "والساعة تشير الئ"+date[3]+ "و"+date[4]+"دقيقة"
tts = gTTS(text=text, lang='ar')
tts.save("time.mp3")
playsound("time.mp3")
