from gtts import gTTS
from io import BytesIO
from playsound import playsound

text="زوبيدا"
name="nameSp"


tts=gTTS(text,"ar")
tts.save("audioBase/"+name+".mp3")
playsound("audioBase/"+name+".mp3")
