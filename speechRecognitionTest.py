import speech_recognition as sr
from playsound import playsound

text=""
r=sr.Recognizer()
with sr.Microphone() as source:
    print("say somethng")
    audio=r.listen(source)
    print("time over, thanks")
try:
    text=r.recognize_google(audio,language='ar')
    print(text)
    file = open("misc/debug/youcommand.txt","w", encoding="utf_8")
    file.write(text)
except:
    pass

if text=="مرحبا":
    print("it read it well")