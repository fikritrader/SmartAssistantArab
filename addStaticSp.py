from gtts import gTTS
from io import BytesIO
from playsound import playsound
import readImageText

text="حسَنًا سأتحدث معكْ"
name="willSpeakSp"


tts=gTTS(text,"ar")
tts.save("audioBase/"+name+".mp3")
playsound("audioBase/"+name+".mp3")
