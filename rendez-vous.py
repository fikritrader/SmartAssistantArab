#--------------#
#--DEPRECATED--#
#--------------#
import speech_recognition as sr
import re
from datetime import datetime
from gtts import gTTS
import playsound
r=sr.Recognizer()
with sr.Microphone() as source:
    print("say somethng")
    audio=r.listen(source)
    print("time over, thanks")
try:
    text=r.recognize_google(audio,language='ar')
    print(text)
except:
    pass
repns = "قم بقول الشهرايضا "

cmdarr=text.split(" ")
# cmdarr=noveau_text.split(" ")
mot1 = "سجل"
mot10 = "\ufeffسجل"
mot11 = "تسجيل"
mot110 = "\ufeffتسجيل"
mot2 = "موعد"
mot3 = "هل"
mot4 = "يوم"
repns1 = "قُمْتُ بِتَسْجِيلِهِ " 
repns2 = "لَمْ اسمع جَيِّدَا"
for i in cmdarr:
    if mot1==i or mot11==i:
        months=["يناير","فبراير","مارس","ابريل","ماي","يونيو","يوليوز","غشت","شتنبر","اكتوبر","نونبر","دجنبر"]
        foundMonth=False
        while(foundMonth == False):
            for month in months:
                if month in text:
                    foundMonth=True
                    monthvalue = months.index(month)+1
                    if monthvalue<= 9:
                        monthvalue="0"+str(monthvalue)
                        noveau_text= text.replace(month,monthvalue)
                        tts=gTTS(repns1,"ar")
                        tts.save("audioBase/repns1.mp3")     
                        playsound("audioBase/repns1.mp3")
                        
                        f=open('monfichier.txt', 'ab')
                        f.write(str(noveau_text+"\n").encode('utf-8')) 
                    break

            if foundMonth==False:
                tts=gTTS(repns,"ar")
                tts.save("audioBase/repns.mp3")     
                playsound("audioBase/repns.mp3")        
    else:
        if mot3==i:
            fichier=open(r"C:/Users/SanaAb/Documents/master/S2/Machine_learning/PROJET/ImageToSpeachPython/monfichier.txt","r",encoding="utf_8").readlines()
            for line in fichier :
                ttt=[]
                ttt=re.findall('\d+', line)
                listtt=[]
                listtt+=ttt
                dateee=listtt[2]+"-"+listtt[1]+"-"+listtt[0]
                maintenant = datetime.now()
                dt=str(maintenant.date())
                if (dateee== dt):
                    type_rendez_vous= line.split(" ")
                    liste_type_rendez_vous=""
                    for x in type_rendez_vous :
                        if x != mot1 and x != mot10  and x != mot11 and x != mot110 and x != mot2 and x != mot4 and not(x.isdecimal()):
                            liste_type_rendez_vous=liste_type_rendez_vous+" "+x
                    outpuText="نَعَمْ لَدَيْكَ مَوْعِدٌ"+liste_type_rendez_vous
                    tts=gTTS(outpuText,"ar")
                    tts.save("audioBase/repns_finale.mp3")     
                    playsound("audioBase/repns_finale.mp3")




    


    
